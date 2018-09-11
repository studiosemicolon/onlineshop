

//==============





function createHeartIc(el) {
	var el = el,
		span = el.querySelector('span'),
		svg = span.querySelector('svg'),
		opacityCurve = mojs.easing.path('M0,0 C0,87 27,100 40,100 L40,0 L100,0'),
		scaleCurve = mojs.easing.path('M0,0c0,80,39.2,100,39.2,100L40-100c0,0-0.7,106,60,106'),
		burst = new mojs.Burst({
			parent: el,
			duration: 1200,
			delay: 200,
			shape: 'circle',
			fill: '#E87171',
			x: '50%', y: '50%',
			opacity: {1:0},
			childOptions: { 
				radius: {6:0},
				type: 'line',
				stroke: '#E87171',
				strokeWidth: 2
			},
			radius: {0:32},
			count: 7,
			//isSwirl: true,
			isRunLess: true,
			easing: mojs.easing.bezier(0.1, 1, 0.3, 1)
		}),
		heart = new Animocon(el, {
			tweens : [
				/* // ring animation
				new mojs.Transit({
					parent: el11,
					duration: 1000,
					delay: 100,
					type: 'circle',
					radius: {0: 95},
					fill: 'transparent',
					stroke: '#C0C1C3',
					strokeWidth: {50:0},
					opacity: 0.4,
					x: '50%',     
					y: '50%',
					isRunLess: true,
					easing: mojs.easing.bezier(0, 1, 0.5, 1)
				}),
				// ring animation
				new mojs.Transit({
					parent: el11,
					duration: 1800,
					delay: 300,
					type: 'circle',
					radius: {0: 80},
					fill: 'transparent',
					stroke: '#C0C1C3',
					strokeWidth: {40:0},
					opacity: 0.2,
					x: '50%',     
					y: '50%',
					isRunLess: true,
					easing: mojs.easing.bezier(0, 1, 0.5, 1)
				}), */
				// icon scale animation
				
				burst,
				
				new mojs.Tween({
					duration : 800,
					easing: mojs.easing.ease.out,
					onUpdate: function(progress) {
						var opacityProgress = opacityCurve(progress);
						span.style.opacity = opacityProgress;

						var scaleProgress = scaleCurve(progress);
						span.style.WebkitTransform = span.style.transform = 'scale3d(' + scaleProgress + ',' + scaleProgress + ',1)';

						var colorProgress = opacityCurve(progress);
						svg.style.fill = colorProgress >= 1 ? '#E87171' : 'none';
						svg.style.stroke = colorProgress >= 1 ? '#E87171' : '#a1a8ad';
					}
				})	
			],
			onUnCheck : function() {
				svg.style.fill = 'none';
				svg.style.stroke = '#a1a8ad';
			}
		});

	return heart;
}


function createCartIc(el) {
	var el = el,
		span = el.querySelector('span'),
		svg = span.querySelector('svg'),
		body = svg.getElementsByTagName("path")[0],
		opacityCurve = mojs.easing.path('M0,0 C0,87 27,100 40,100 L40,0 L100,0'),
		scaleCurve = mojs.easing.path('M0,0c0,80,39.2,100,39.2,100L40-100c0,0-0.7,106,60,106'),
		burst = new mojs.Burst({
			parent: el,
			duration: 1200,
			delay: 200,
			shape: 'circle',
			fill: '#111111',
			x: '50%', y: '50%',
			opacity: {1:0},
			childOptions: { 
				radius: {6:2},
				type: 'line',
				stroke: '#111111',
				strokeWidth: 2
			},
			radius: {0:36},
			angle: 45,
			count: 4,
			//isSwirl: true,
			isRunLess: true,
			easing: mojs.easing.bezier(0.1, 1, 0.3, 1)
		}),
		heart = new Animocon(el, {
			tweens : [
				/* // ring animation
				new mojs.Transit({
					parent: el11,
					duration: 1000,
					delay: 100,
					type: 'circle',
					radius: {0: 95},
					fill: 'transparent',
					stroke: '#C0C1C3',
					strokeWidth: {50:0},
					opacity: 0.4,
					x: '50%',     
					y: '50%',
					isRunLess: true,
					easing: mojs.easing.bezier(0, 1, 0.5, 1)
				}),
				// ring animation
				new mojs.Transit({
					parent: el11,
					duration: 1800,
					delay: 300,
					type: 'circle',
					radius: {0: 80},
					fill: 'transparent',
					stroke: '#C0C1C3',
					strokeWidth: {40:0},
					opacity: 0.2,
					x: '50%',     
					y: '50%',
					isRunLess: true,
					easing: mojs.easing.bezier(0, 1, 0.5, 1)
				}), */
				// icon scale animation
				
				burst,
				
				new mojs.Tween({
					duration : 800,
					easing: mojs.easing.ease.out,
					onUpdate: function(progress) {
						var opacityProgress = opacityCurve(progress);
						span.style.opacity = opacityProgress;

						var scaleProgress = scaleCurve(progress);
						span.style.WebkitTransform = span.style.transform = 'scale3d(' + scaleProgress + ',' + scaleProgress + ',1)';

						var colorProgress = opacityCurve(progress);
						body.style.fill = colorProgress >= 1 ? '#111111' : 'none';
						svg.style.stroke = colorProgress >= 1 ? '#111111' : '#a1a8ad';
					}
				})	
			],
			onUnCheck : function() {
				body.style.fill = 'none';
				svg.style.stroke = '#a1a8ad';
			}
		});

	return heart;
}


var hearts = document.getElementsByClassName('pnl-favorites'),
	carts = document.getElementsByClassName('pnl-tocart');

for (var i=0;i<hearts.length;i++) {
	createHeartIc(hearts[i].querySelector('div'));
	createCartIc(carts[i].querySelector('div'));
}