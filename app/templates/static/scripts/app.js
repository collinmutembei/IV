angular.module('pheditApp', ['ngRoute', 'auth0', 'angular-storage', 'angular-jwt', 'angulartics', 'angulartics.google.analytics']);

angular.module('pheditApp').config(function (authProvider) {
  authProvider.init({
    domain: 'solublecode.auth0.com',
    clientID: '0RobeRw5JMnTMxtxzLAm3RxGhLQbyzN4'
  });
})
.run(function(auth) {
  // This hooks all auth events to check everything as soon as the app starts
  auth.hookEvents();
});

angular.module('pheditApp').config(function($routeProvider, $analyticsProvider){
    $routeProvider
        .when('/', {
            templateUrl: 'static/pages/landing.html'
        }).when('/app', {
            templateUrl: 'static/pages/dashboard.html'
        }).when('/test', {
            templateUrl: 'static/pages/test.html'
        }).otherwise({
            redirectTo: '/'
        });
});
