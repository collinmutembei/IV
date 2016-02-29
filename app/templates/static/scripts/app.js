var app = angular.module('pheditApp', ['ngFileUpload']);

app.config(function($httpProvider) {

    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

});

app.controller('MyCtrl', ['$scope', 'Upload', function ($scope, Upload) {

    $scope.message = "drop image file here or click to upload";

    // upload on file select or drop
    $scope.upload = function (file) {
        Upload.upload({
            url: '/api/images/',
            data: {'image': file}
        }).then(function (resp) {
            $scope.message = "loading...";
            console.log('file uploaded successfully');
        }, function (resp) {
            console.log('file uploaded error: ' + resp.status);
        });
    };
}]);
