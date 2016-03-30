angular.module('pheditApp').factory('MainService', function ($resource) {
    return {
        all_images: $resource('/api/images/', {}, {
            getImages: {
                method: 'GET',
                isArray: true
            }
        }, {
            stripTrailingSlashes: false
        }),
        image_effects: $resource('/api/phedited/', {}, {
            send_effects: {
                method: 'POST'
            },
            get_effects: {
                method: 'GET',
                isArray: true
            }
        }, {
            stripTrailingSlashes: false
        }),
        saved_images: $resource('/api/saved/', {}, {
            save: {
                method: 'POST'
            },
            get_saved: {
                method: 'GET',
                isArray: true
            }
        }, {
            stripTrailingSlashes: false
        })
    };
});
