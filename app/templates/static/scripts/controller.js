angular.module('pheditApp').controller('MyCtrl', ['$scope', 'Upload', 'MainService', function ($scope, Upload, MainService) {

    $scope.$on('uploadComplete', function () {
        $scope.images = MainService.all_images.getImages();
    });

    $scope.upload = function (file) {
        Upload.upload({
            url: '/api/images/',
            data: {'image': file}
        }).then(function (resp) {
            var $button = $("button");
            $button.parent().addClass("clicked").delay(2600).queue(function(){
                $(this).addClass("success");
            });
            $scope.$emit('uploadComplete');
            console.log('file uploaded successfully');
        }, function (resp) {
            console.log('file uploaded error: ' + resp.status);
        });
    };
}]);
