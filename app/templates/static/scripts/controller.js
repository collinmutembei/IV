angular.module('pheditApp').controller('MyCtrl', ['$scope', 'Upload', 'MainService', function ($scope, Upload, MainService) {

    $scope.imageuploaded = false;

    $scope.upload = function (file) {
        Upload.upload({
            url: '/api/images/',
            data: {'image': file}
        }).then(function (response) {
            $scope.imageuploaded = true;
            $scope.$emit('uploadComplete');
            console.log('photo uploaded successfully');
        }, function (error) {
            console.log('photo uploaded error: ' + error.status);
            //file fails to upload, display error message
        });
    };

    $scope.$on('uploadComplete', function () {
        MainService.all_images.getImages().
        $promise.
        then(function(result){
            $scope.effectsModel = {}
            $scope.images = result
            $scope.original_image = result[result.length - 1].image
            $scope.imageurl = $scope.original_image
            $scope.$emit('sharable_url');
        }).
        catch(function(response){
            console.log("failed to fetch images");
        });
    });

    $scope.$watchCollection('effectsModel', function () {
        $scope.applyeffects = [];
        angular.forEach($scope.effectsModel, function (value, key) {
            if (value) {
                $scope.applyeffects.push(key);
            }
        });
        $scope.$emit('addeffect');
    });

    $scope.$on('addeffect', function () {
        if ($scope.original_image && $scope.applyeffects.length > 0) {
            MainService.image_effects.send_effects({'original_image_url': $scope.original_image, 'effects': $scope.applyeffects}).
            $promise.
            then(function (result) {
                $scope.imageurl = result.phedited_image;
                $scope.$emit('sharable_url');
            }).
            catch(function (response) {
                console.log("failed to apply effects");
            });
        } else {
            $scope.imageurl = $scope.original_image
            $scope.share_url = $scope.imageurl
        }
    });

    $scope.$on('sharable_url', function () {
        $scope.share_url = $scope.imageurl
    })

    $scope.share_image = function () {
        FB.ui(
            {
                method: 'feed',
                link: $scope.share_url,
                caption: '#phedited'
            }, function (response) {
            }
        );
    };

    $scope.clear_canvas = function() {
        $scope.$emit('canvascleared');
    }

    $scope.$on('canvascleared', function () {
        $scope.imageurl = ""
        $scope.share_url = ""
        $scope.imageuploaded = false;
    });
}]);
