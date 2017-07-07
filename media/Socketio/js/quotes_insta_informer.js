function initSocketMain()
{
	socket = io.connect('qrt3.instaforex.com:8443/', {secure: true});

	socket.on('connect', function (data) 
	{						
		socket.emit('subscribe', needQuotes);
	});
	
	socket.on('close', function () 
	{		        
        socket.emit('unsubscribe', needQuotes);
	});

	socket.on('disconnect', function () 
	{        
        socket.emit('unsubscribe', needQuotes);        
	});
	
	socket.on('quotes', function (data) 
	{		
    var quote = data.msg;  
		var bid = getPrice(quote.bid, quote.digits);
		var ask = getPrice(quote.ask, quote.digits);

		if($("li[id^='symbol_']", $("#quotes")).length > 0) {
			var symbol ="#symbol_" + quote.symbol;
			$(symbol + " img.arrow").attr("src",img_http+"site/informer/"+getClassDirection(quote.change)+".png");
			$(symbol + " p.quote_ask").html(ask);
			$(symbol + " p.quote_bid").html(bid);
		}
	});
}

function getClassDirection(val)
{
	return (val < 0 ? 'red' : 'green');
}

function getPrice(val, digits)
{
	return retVal = (val.toFixed(digits)).toString();
}

$(document).ready(function(){
	$('#quotes_informer').css({'height':$('#quotes li').innerHeight()}); //Поправка высоты информера для разного маштаба в браузере
	var startscroll = setInterval(scroll_quotes,5000);
	var all_spreads = false;
	$('#all-spreads').click(
		function(){
				if (all_spreads)
				{
					$('#quotes_informer').animate({'height':$('#quotes li').innerHeight()});
					startscroll = setInterval(scroll_quotes,5000);	
				}
				else
				{
					$('#quotes_informer').animate({'height':$('#quotes').innerHeight()});	
					clearInterval(startscroll);
				}
				all_spreads=!all_spreads;
		}
	);

	function scroll_quotes() { 
		$('#quotes').animate(
			{'top':'-'+$('#quotes li').innerHeight()},
			1000, 
			"linear", 
			function(){
				$('#quotes').append($('#quotes').children('li:lt(6)'));
				$('#quotes').css({'top':'0px'});
				$('#quotes_informer').css({'height':$('#quotes li').innerHeight()}); //Поправка высоты информера для разного маштаба в браузере
			}
		);
	}
});

