var app = angular.module('pheditApp', ['ngResource', 'ngFileUpload']);

app.config(function($httpProvider) {

    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

});
