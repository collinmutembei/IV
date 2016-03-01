angular.module('pheditApp').factory('MainService', function($resource) {
    return {
        all_images: $resource('/api/images/', {}, {
            getImages: {
                method: 'GET',
                isArray: true
            }
        }, {
            stripTrailingSlashes: false
        })
    };
});
