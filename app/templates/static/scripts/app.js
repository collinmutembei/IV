var app = angular.module('pheditApp', ['ngResource', 'ui.bootstrap', 'ngFileUpload']);

app.config(function($httpProvider) {

    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

});

$(document).ready(function(){
    $('.share-button').on('click',function(){
        $(this).addClass('open');
    })
    // $( ".share-items" ).draggable({
    //     axis: "x",
    //     containment : ".share-items-wrapper"
    // });
    $( ".share-item" ).on('click',function(){
        $('.share-button').addClass('shared');
        setTimeout(function(){
            $('.share-button').addClass('thankyou');
        }, 800);
        setTimeout(function(){
            $('.share-button').removeClass('open');
            $('.share-button').removeClass('shared');
            $('.share-button').removeClass('thankyou');
        }, 2500);
    });

});
