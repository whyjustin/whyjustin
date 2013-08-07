$(function() {
	var windowHeight = $(window).height();
	var width = windowHeight * 361 / 448;
	var pacmanElement = $('.pacman');
	pacmanElement.width(width);
	PACMAN.init(pacmanElement[0], "./");
});