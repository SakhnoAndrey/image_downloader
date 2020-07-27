 #!/usr/bin/python

 # начинаем скрипт с переменных конфигурации

 source_folder = ' ' # каталог с html-файлами внутри которых есть линки вида img.auctiva.com/imgdata/8/4/0/3/3/0/webimg/815355468_o.gif
 image_folder = ' '  # каталог куда надо скачать картинки со всей вложеностью подкаталогов imgdata/8/4/0/3/3/0/webimg/815355468_o.gif по линкам из файлов
 newsite_name = ' '  # имя сайта, на которое надо поменять img.auctiva.com в коде файлов в goal_folder
 goal_folder = ' '   # каталог с файлами-копиями из source_folder, но с измененными линками с img.auctiva.com на newsite_name, файлы в source_folder не меняем

 

 ############### Вторая фаза изменений, первичная обработка файла, необходимо выполнять до первой фазы

 ### 1) заменяем все подобные случаи 
    <div style="background-image:url(&#39;https://img.auctiva.com/imgdata/_путь_к_картинке&#39;)"></div>
 # на
    <div class="img-result" style="background-image: url('https://img.auctiva.com/imgdata/_путь_к_картинке');"></div>

 # пример: меняем

 <div style="background-image:url(&#39;https://img.auctiva.com/imgdata/8/4/0/3/3/0/webimg/884485331_o.jpg&#39;)"></div>
 # на 
 <div class="img-result" style="background-image: url('https://img.auctiva.com/imgdata/8/4/0/3/3/0/webimg/884485331_o.jpg');"></div>


 ### 2) заменяем

 <p>We post items next business day after payment.
 <p>International shipping by <strong>Ukrposhta (Registered Airmail Service)</strong> usually takes about <strong>10-14</strong> days to most countries, but in some cases delays can cause delivery times up to <strong>30</strong> days or even more.</p>
 <p>We can not take responsibility for international shipments what are lost or delayed.</p>
 <p>However, we will do everything we can to help trace shipment delayed more than 30 days.</p>
 # на
 <p>We make every effort to process your orders quickly. Our standard shipping method is <strong>Registered Airmail requiring recipient’s signature upon the delivery.</strong></p>
 <p>All orders are usually dispatched within <strong>1-2 business days.</strong></p>
 <p>Once your order has been dispatched, an estimated delivery time will be subject to the delivery service but depending on location it is about <strong>14-20 business days.</strong></p>
 <p>Delivery times are estimates and commence from the date of shipping, rather than the date of order. Please note that the delivery of international orders may take longer than expected due to customs or other issues.</p>
 <p>Our shipping method comes with tracking and your tracking number will be provided once your order has been posted.</p>
 <p>If you have any questions about the delivery and shipment or your order, please contact us at any time via <strong><a target="_blank" href="https://contact.ebay.com/ws/eBayISAPI.dll?FindAnswers&requested=lyapko_applicators">eBay contact form</a></strong>.</p>


### 3) заменяем

<p>PLEASE E-MAIL US BEFORE LEAVING NEGATIVE FEEDBACK, OR OPEN ANY DISPUTE ON eBAY, IT WILL JUST UPSET AND HURT BOTH SIDES.</p>
# на
<p>Please e-mail us before leaving negative feedback, or open any dispute on eBay. We will do our best to solve the issue for you. </p>


### 4) заменяем везде, если находим

http:
# на 
https:

### 6) заменяем
<div>
				<input type="radio" name="t_switch" checked>
				<label style="margin-top:0px">
# на (если это первый совпадение)
<div class="slider">
				<input type="radio" name="t_switch" id="id1" checked="checked" />
				<label for="id1" class="head-label" style="margin-top: 0px;">
# иначе на (таких замен будет несколько, надо для каждой следующей делать id+1, т.е. для второй замены id2 для третьей id3. Для каждой сдедущей замены 
# начение margin-top увеличмвается на 140px)
<input type="radio" name="t_switch" id="id2"/>
				<label for="id2" class="head-label" style="margin-top: 140px;">


### 7) заменяем
<div>
					<input type="radio" name="p_switch_1" checked>
					<label>
# на
<div class="sub-slider">
					<input type="radio" name="p_switch_1" id="p_id1" checked="checked"/>
					<label for="p_id1">


### 8) заменяем (таких замен будет несколько, надо для каждой следующей делать p_id+1, т.е. для второй замены p_id3 для третьей p_id4)
<input type="radio" name="p_switch_1">
					<label>
# на
<input type="radio" name="p_switch_1" id="p_id2"/>
					<label for="p_id2">


### 9) заменяем
<input type="radio" name="p_switch_2" checked>
					<label>
# на
<div class="sub-slider">
					<input type="radio" name="p_switch_2" id="p_id21" checked="checked"/>
					<label for="p_id21">


<### 10) заменяем (таких замен будет несколько, надо для каждой следующей делать p_id+1, т.е. для второй замены p_id23 для третьей p_id24 и т.д.)
<input type="radio" name="p_switch_2">
					<label>
# на
<input type="radio" name="p_switch_2" id="p_id22"/>
					<label for="p_id22">


### 11) заменяем
<input type="radio" name="p_switch_3" checked>
					<label>
# на
<div class="sub-slider">
					<input type="radio" name="p_switch_3" id="p_id41" checked="checked"/>
					<label for="p_id41">


### 12) заменяем (таких замен будет несколько, надо для каждой следующей делать p_id+1, т.е. для второй замены p_id43 для третьей p_id44 и т.д.)
<input type="radio" name="p_switch_3">
					<label>
# на
<input type="radio" name="p_switch_3" id="p_id42"/>
					<label for="p_id42">


### 13) заменяем (таких замен будет несколько, надо для каждой следующей делать pic- +1, т.е. для второй замены pic-2 для третьей pid-3 и т.д.)
<input type="checkbox">
			<label><img src=
# на
<input type="checkbox" id="pic-1"/>
			<label for="pic-1" class="lightbox"><img src=


### 14) заменяем
<div style="display:flex">
# на
<div style="display: flex; flex-wrap: wrap; justify-content: center;">


### 15) после первого нахождения условия 14), все комбинации (таких замен будет несколько, надо для каждой следующей делать pic- +1, т.е. для второй замены pic-2 для третьей pid-3 и т.д.)
<label>
					<div>
						<p>*
# менять на
<label for="pic-1" class="grid-item">
					<div class="link-gallery">
						<p>*


### 16) заменяем
<div></div>
			<h2>Our Store</h2>

# на
</section>
		<section id="content2">
			<div class="block-title"></div>
			<h2 class="head">Our Store</h2>
			

### 17) после второго нахождения условия 14), все комбинации
<div>
					<p>*
# менять на			
		<div class="link-store">
					<p>*


### 18) заменяем
<div></div>
			<h2>Payment Policy</h2>
			<h4><strong>We only accept PayPal payments.</strong></h4>
			<p><strong>For PayPal payments please go to   <a href="https://www.paypal.com" target="_blank">www.PayPal.com</a></strong></p>
		
		
			<div></div>
			<h2>Shipping Policy</h2>
# на
</section>
		<section id="content3">
			<div class="block-title"></div>
			<h2 class="head">Payment Policy</h2>
			<h4><strong>We only accept PayPal payments.</strong></h4>
			<p><strong>For PayPal payments please go to www.PayPal.com</a></strong></p>
		</section>
		<section id="content4">
			<div class="block-title"></div>
			<h2 class="head">Shipping Policy</h2>


### 18) заменяем
<div></div>
			<h2>Return Policy</h2>
# на
</section>
		<section id="content5">
			<div class="block-title"></div>
			<h2 class="head">Return Policy</h2>


### 18) заменяем
<div></div>
			<h2>Feedback Policy</h2>
# на
</section>
		<section id="content6">
			<div class="block-title"></div>
			<h2 class="head">Feedback Policy</h2>


### 18) заменяем
</p></div>
	<div></div>
</body></html>
# на
</section>
	</div>
	<div class="bgr-top"></div>
</main>