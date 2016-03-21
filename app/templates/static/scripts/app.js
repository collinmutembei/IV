angular.module('pheditApp', ['ngRoute']);

angular.module('pheditApp').config(function($routeProvider){
    $routeProvider
        .when('/', {
            templateUrl: 'static/pages/landing.html'
        }).when('/app/', {
            templateUrl: 'static/pages/dashboard.html'
        });
});
