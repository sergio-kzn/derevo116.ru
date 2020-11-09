document.addEventListener('DOMContentLoaded', function () {

    let button = document.getElementById('add-to-basket');
    let ul = document.getElementById('basket-list')
    let basket_count = parseInt(document.getElementById("basket-count").textContent, 10);
    let basket_sum = parseInt(document.getElementById("basket-sum").textContent, 10);
    let li_empty = document.getElementById('empty-basket');

    let toastElList = [].slice.call(document.querySelectorAll('.toast'))
    let toastList = toastElList.map(function (toastEl) {
        return new bootstrap.Toast(toastEl)
    })

    button.addEventListener('click', async function () {
        // проверка выбор цвета
        if (button.hasAttribute('data-color-check') && !button.hasAttribute('data-color'))
            toastList[1].show();
        else {

            // отправляем ПОСТ на серевер, что бы обновить сессию //
            let color = "";
            let options_in_item = '';
            let price = 0;

            if (button.hasAttribute('data-color')) {
                color = button.getAttribute('data-color');
            }

            for (let i = 1; i <= button.getAttribute('data-max-options'); i++)
                if (button.hasAttribute('data-price-option-' + i)) {
                    let title_option = button.getAttribute('data-title-option-' + i)
                    let option = button.getAttribute('data-option-' + i)
                    options_in_item += title_option + ': ' + option + '<br>';
                    price += parseInt(button.getAttribute('data-price-option-' + i).replace(/\s+/g, ''), 10);
                }

            if (button.hasAttribute('data-price-product')) {
                price += parseInt(button.getAttribute('data-price-product').replace(/\s+/g, ''), 10);
            }

            let data = {
                'id': button.getAttribute("data-product-id"),
                'li_id': 'item_' + basket_count,
                'title': button.getAttribute("data-title"),
                'title_href': button.getAttribute('data-url'),
                'color': button.getAttribute('data-color'),
                'options': options_in_item,
                'count': button.getAttribute("data-count"),
                'price': price,
            };

            let response = await fetch('/cart/addtocart/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json;charset=utf-8'
                },
                body: JSON.stringify(data)
            });

            if (response.ok) {

                document.querySelector('#basket').innerHTML = await response.text();

                document.querySelector('.toast-body').innerHTML =
                    '<span class="font-weight-bolder mb-1" style="font-size: large">' + button.getAttribute("data-title") + '</span>' + '<br>'
                    + button.getAttribute("data-count") + ' шт. <br>'
                    + color + options_in_item + 'Цена: <b>' + price + ' &#x20bd;</b>';

                toastList[0].show();
            }

            // console.log(result);

            ////////////////////////////////////////////////////////////////
            // let li = document.createElement('li');
            // li.classList.add('list-group-item', 'list-group-item-action', 'px-1');
            //
            // // название товара
            // let div_title = document.createElement('div');
            // let title = button.getAttribute("data-title");
            // let a_title = document.createElement('a');
            // let a_url = button.getAttribute('data-url');
            // div_title.classList.add('basket-list-title-item', 'd-flex', 'justify-content-between');
            // a_title.classList.add('text-decoration-none', 'text-dark', 'font-weight-bolder', 'mb-1');
            // a_title.href = a_url;
            // a_title.textContent = title;
            //
            // // количество
            // let span_count = document.createElement('span');
            // let count = button.getAttribute("data-count");
            // span_count.classList.add('badge', 'bg-primary', 'rounded-pill', 'basket-list-count', 'h-25');
            // span_count.textContent = count;
            //
            // // опции
            // let div_options = document.createElement('div');
            // div_options.classList.add('basket-list-options', 'text-muted', 'small', 'd-flex', 'justify-content-between', 'align-items-center')
            //
            // let div_color = document.createElement('div');
            // div_color.classList.add('basket-list-color');
            // let color = "";
            // let options_in_item = '';
            // let price = 0;
            // let price_span = '';
            // if (button.hasAttribute('data-color')) {
            //     color = 'Цвет: ' + button.getAttribute('data-color') + '<br>';
            // }
            //
            // let max_options = button.getAttribute('data-max-options')
            // for (let i = 1; i <= max_options; i++)
            //     if (button.hasAttribute('data-price-option-' + i)) {
            //         let title_option = button.getAttribute('data-title-option-' + i)
            //         let option = button.getAttribute('data-option-' + i)
            //         options_in_item += title_option + ': ' + option + '<br>';
            //         price += parseInt(button.getAttribute('data-price-option-' + i).replace(/\s+/g, ''), 10);
            //     }
            //
            // // цена без опций
            // if (button.hasAttribute('data-price-product')) {
            //     price += parseInt(button.getAttribute('data-price-product').replace(/\s+/g, ''), 10);
            // }
            // price_span = '<span>Цена: <b>' + price + ' &#x20bd;</b></span>';
            // div_color.innerHTML = color + options_in_item + price_span;
            //
            // // удалить [ х ]
            // let span_delete = document.createElement("span");
            // span_delete.classList.add('btn', 'btn-outline-danger', 'btn-sm', 'delete_from_basket');
            // span_delete.setAttribute('role', 'button');
            // span_delete.textContent = ' x ';
            //
            // div_title.appendChild(a_title);
            // div_title.appendChild(span_count);
            // div_options.appendChild(div_color);
            // div_options.appendChild(span_delete);
            // li.appendChild(div_title);
            // li.appendChild(div_options);
            // ul.appendChild(li);
            //
            // // убираем заглушку
            // li_empty.classList.add('d-none');
            //
            // basket_count += 1;
            // basket_sum += price * parseInt(count, 10);
            // update_count_and_price(basket_count, basket_sum)
            //
            // li.id = 'item_' + basket_count;
            // span_delete.onclick = delete_item_from_basket('item_' + parseInt(basket_count), count, price)
            // span_delete.onclick = function () {
            //     delete_item_from_basket(li.id, basket_count, basket_sum)
            // };

            // всплывающее сообщение


        }
    })

    // функция удалить товар из корзины
    window.delete_item_from_basket = function (li_id, current_count, current_price) {
        let current_li = document.querySelector('#' + li_id);
        // let current_count = parseInt(current_li.firstChild.lastChild.textContent.replace(/\s+/g, ''), 10)
        // let current_price = parseInt(current_li.lastChild.firstChild.lastChild.textContent.replace(/\s+/g, ''), 10);

        // basket_count -= 1;
        // basket_sum -= current_price * current_count;
        if (current_li)
            current_li.remove();

        // update_count_and_price(basket_count, basket_sum)
    };

    // функция обновляет цену и количество товаров в корзине
    let update_count_and_price = function (count, sum) {
        let span_basket_count = document.getElementById("basket-count");
        let span_basket_sum = document.getElementById("basket-sum");
        let span_basket_sum_footer = document.getElementById("basket-sum-footer");

        span_basket_count.textContent = count;
        span_basket_sum.textContent = sum;
        span_basket_sum_footer.innerHTML = 'Сумма: <b>' + sum + ' &#x20bd;</b>';
        if (count < 1) li_empty.classList.remove('d-none');
    }
})