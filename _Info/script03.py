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


### 19) заменяем
<div></div>
	<div>
		<img src="https://pipes2go.com/upload/ebp/img/top_img2.png
# на
<main>
	<div class="bgr-top"></div>
	<div id="wrapper">
		<img src="https://pipes2go.com/upload/ebp/img/top_img2.png


### 20) добавляем в начало файла

<style>
	main {
		min-width: 320px;
		max-width: 100%;
		padding: 0;
		margin: 0 auto;
		background-image: url('https://pipes2go.com/upload/ebp/img/bgr.png');
		font-family: "Times New Roman";
	}

	#wrapper {
		width: 891px;
		margin: 0 auto;
	}

	.bgr-top {
		width: 100%;
		height: 163px;
		background-image: url('https://pipes2go.com/upload/ebp/img/bgr_line.png');
		background-repeat: repeat-x;
	}

	.bgr-menu {
		width: 761px;
		height: 55px;
		position: absolute;
    	margin: 3px 0 0 66px;
		background-image: url('https://pipes2go.com/upload/ebp/img/menu_bgr6.png');
		background-repeat: repeat-x;
	}

	section {
		display: none;
		padding: 20px 0 0;
	}

	input {
		display: none;
	}

	label {
		float:left;
		position: relative;
   	 	z-index: 1;
	    color: #442500;
	    font-size: 20px;
	    /*font-family: Arial;*/
	    font-weight: 700;
	    text-align: center;
	    width: 115px;
	    margin-top: 7px;
	    text-shadow: 0px 1px 2px #f1e39e;
	    cursor: pointer;
	    border-bottom: 2px solid transparent;
	}

	label:hover {
		text-decoration: underline;
	}

	input:checked + label {
		color: #1f1101;
	}

	#tab1:checked ~ #content1,
	#tab2:checked ~ #content2,
	#tab3:checked ~ #content3,
	#tab4:checked ~ #content4,
	#tab5:checked ~ #content5,
	#tab6:checked ~ #content6 {
		display: block;
	}

	.block-title {
		width: 96%;
    	height: 34px;
    	margin: 0 auto;
    	padding: 12px 0 0 0;
		background-image: url('https://pipes2go.com/upload/ebp/img/ls_bl_title_fill.png');
		background-repeat: repeat-x;
	}

	.head {
		color: #f1e39e;
	    font-size: large;
	    /*font-family: Verdana;*/
	    text-align: left;
	    font-weight: 700;
	    text-shadow: 1px 1px 2px black;
		position: absolute;
    	margin: -35px 0 0 20px;
	}

	.block-title:before {
		content: "";
	    position: absolute;
	    margin: -12px 0 0 -16px;
	    width: 16px;
	    height: 46px;
	    background-image: url(https://pipes2go.com/upload/ebp/img/ls_bl_title_left.png);
	    background-repeat: no-repeat;
	}

	.block-title:after {
		content: "";
		position: absolute;
		margin: -12px 0 0 855px;
		width: 16px;
		height: 46px;
		background-image: url('https://pipes2go.com/upload/ebp/img/ls_bl_title_right.png');
		background-repeat: no-repeat;
	}

	h1 {
		color: #442500;
    	font-weight: normal;
    	text-align: center;
	}

	h2 {
		color: #442500;
    	font-weight: bold;
    	text-align: left;
	}

	h3 {
		color: #442500;
    	font-weight: bold;
    	font-size: 16px;
    	text-align: left;
    	text-transform: uppercase;
	}

	h4 {
		color: #442500;
    	font-weight: normal;
    	text-align: center;
    	font-size: 21px;
		letter-spacing: 2px;
	}

	p {
		color: #442500;
	    font-weight: normal;
	    text-align: left;
	    font-size: 19px;
	    letter-spacing: 1px;
	    line-height: 27px;
	    /*font-family: Tahoma;*/
	}

	.red {
		color: #b90303;
	}

	.green {
		color: green;
	}

	.blue {
		color: blue;
	}

	.link-store, .link-gallery {
	    width: 200px;
	    margin: 20px;
	    background-color: #d9cece;
	    border-top: 1px solid #663333;
	    border-bottom: 1px solid #663333;
	    border-left: 6px solid #663333;
	    border-right: 6px solid #663333;
	}

	.link-store img, .link-gallery img {
		max-width: 100%;
		width: 200px;
		height: 160px;
		margin-bottom: 8px;
	}

	.link-gallery {
	    width: 200px;
	    margin: 5px;
	}

	.link-gallery img {
		max-width: 100%;
		width: 200px;
		height: 160px;
	}

	.link-store p, .link-gallery p {
		font-weight: bold;
	    /*font-family: verdana, 'sans serif';*/
	    background-color: #d9cece;
	    color: #663333;
	    text-align: center;
	    font-size: 16px;
	    height: 20px;
	    margin: 17px 0 0 0;
	    padding: 0;
	    line-height: 0px;
	}

	.link-store small {
		width: 135px;
		color: #333333;
	    text-align: left;
	    margin: 0 5px 0 10px;
	    font-size: 12px;
	    float: left;
	}

	.link-store small {
		width: 135px;
		color: #333333;
	    text-align: left;
	    margin: 0 5px 0 10px;
	    font-size: 12px;
	    float: left;
	}

	.link-store .link {
		width: 30px;
    	height: 30px;
	}

	.grid-item {
	  width: 25%;
	  opacity: .95;
	  -webkit-transition: opacity .5s;
	          transition: opacity .5s;
	    float: none;
	    position: static;
	    
	    margin-top: 0;
	    text-shadow: none;
	    cursor: pointer;
	    border: none;
	}

	.grid-item:hover {
	  opacity: 1;
	  text-decoration: none;
	}

	.lightbox {
	  width: 100%;
	  position: fixed;
	  top: 0;
	  left: 0;
	}

	.lightbox {
	  z-index: 2;
	  min-height: 100%;
	  overflow: auto;
	  -webkit-transform: scale(0);
	      -ms-transform: scale(0);
	          transform: scale(0);
	  -webkit-transition: -webkit-transform .5s ease-out;
	          transition: transform .5s ease-out;
	}

	.lightbox img {
	  position: fixed;
	  top: calc(1000px + 50%);
	  left: 50%;
	  max-width: 56%;
	  max-height: 56%;
	  -webkit-transform: translate(-50%, -50%);
	      -ms-transform: translate(-50%, -50%);
	          transform: translate(-50%, -50%);
	  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.25);
	}

	input[type="checkbox"]:checked + .lightbox {
	  -webkit-transform: scale(1);
	      -ms-transform: scale(1);
	          transform: scale(1);
	}

	.slider {
		width: 100%;
		margin: 10px auto 50px auto;
	}

	.slider .sub-slider>img {
		margin-top: 480px;
		position: absolute;
		width: 800px;
		left: 0;
	}

	.slider label {
	    float: left;
	    position: static;
	    width: auto;
	    height: 60px;
	    border: none;
	    background-color: #FFF;
	}

	.slider .head-label {
		position: absolute;
    	margin: 0 0 0 575px;
		border-top: none;
		border-right: 5px solid transparent;
		border-bottom: none;
		border-left: 5px solid #AAA;
		height: 130px;
	}

	.slider .sub-slider label {
		width: 110px;
		height: 110px;
		filter: grayscale(1);
		-moz-filter: grayscale(1);
		-o-filter: grayscale(1);
	}

	.slider .sub-slider label img {
		max-width: 100%;
		max-height: 100%;
	}

	.slider input[name="t_switch"] {
		display: none;
	}

	.sub-slider {
		display: none;
		width: 570px;
		position: absolute;
	    padding-top: 19px;
	    background-color: #FFF;
    	flex-wrap: wrap;
    	align-items: center;
		border: 5px solid #aaa;
	}

	.img-result {
		background-repeat: no-repeat; 
		background-size: contain; 
		width: 830px; 
		height: 470px; 
		background-color: #FFF;
		position: absolute; 
		top: 500px;
	}

	.slider input[name="t_switch"]:checked + label {
		border-top: 5px solid #AAA;
		border-right: 5px solid #AAA;
		border-bottom: 5px solid #AAA;
		border-left: none;
	}

	.slider input[name="t_switch"]:checked + label + .sub-slider{
		display: flex;
	}

	.slider input[name="p_switch_1"]:checked + label {
		filter: grayscale(0);
	}

	.slider input[name="p_switch_2"]:checked + label {
		filter: grayscale(0);
	}

	.slider input[name="p_switch_3"]:checked + label {
		filter: grayscale(0);
	}

	.slider input[name="p_switch_1"] ~ .img-result {
		opacity: 0;
	}

	.slider input[name="p_switch_1"]:checked + label + .img-result {
		opacity: 1;
	}

	.slider input[name="p_switch_2"] ~ .img-result {
		opacity: 0;
	}

	.slider input[name="p_switch_2"]:checked + label + .img-result {
		opacity: 1;
	}

	.slider input[name="p_switch_3"] ~ .img-result {
		opacity: 0;
	}

	.slider input[name="p_switch_3"]:checked + label + .img-result {
		opacity: 1;
	}
	
</style>
