	jQuery(document).ready(function() {
		$('#layerslider').layerSlider({
			skinsPath : '../static/layerslider/skins/',
			skin : 'fullwidth',
			thumbnailNavigation : 'hover',
			hoverPrevNext : true,
			autoPlayVideos          : false,
			responsive : true,
			responsiveUnder : 1170,
			sublayerContainer : 1170,
			showCircleTimer     : false,
		});
		
	$('.main-slider').flexslider({
        slideshow: false
      });
	
  
	  $('.typeahead').typeahead()
	  
      $('.for-mans, .for-womans, .clients').flexslider({
        animation: 'slide',
        slideshow: true,
        animationLoop: true,
        controlNav: false
      });
      $('.recent-blog, .testimonials').flexslider({
        animation: 'slide',
        slideshow: false,
        animationLoop: false,
        controlNav: false
      });
	  
	$("#countdown").countdown({
		date: "23 december 2013 23:59:59", // add your date here.
		format: "on"
	},
	function() { 
		alert("done!") 
	});		
		
	$(function () {
		$('#wdtTab a:first').tab('show');
	})
	
	
		$(".hover").hover(
		function () {
			$("ul.topcart").slideDown(500);
		}, 
		function () {
			$("ul.topcart").slideUp(500);
		}
	);


    $('.social, .store-categories, .display').tooltip({
      selector: "a[data-toggle=tooltip]"
    })

    $('.social, .store-categories, .display').tooltip()
	
	});
	
	jQuery(window).scroll(function(){
		if (jQuery(this).scrollTop() > 1) {
			jQuery('.wdttop').css({bottom:"25px"});
		} else {
			jQuery('.wdttop').css({bottom:"-100px"});
		}
	});
	jQuery('.wdttop').click(function(){
		jQuery('html, body').animate({scrollTop: '0px'}, 800);
		return false;
	});
	
jQuery(document).ready(function() {
	jQuery(document).find('.wdt-product').each(function(i, widget) {
		widget = jQuery(widget);
		
		if(!widget.hasClass('active')) {
			widget.addClass('active');
			wdtGallery(widget);
		}
		
	});
});

var wdtGallery = function(widget) {
	
	widget.find('.wdt-product').each(function(i, img) {
		img = jQuery(img);
		
		img.mouseenter(function() {
			widget.attr('data-stop', 1);
			img.addClass('hover');
		});
		
		img.mouseleave(function() {
			widget.attr('data-stop', 0);
			img.removeClass('hover');
		});		
		});
};