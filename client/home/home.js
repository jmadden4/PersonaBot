'use strict';

angular.module('myApp.home', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/home', {
    templateUrl: 'home/home.html',
    controller: 'HomeCtrl'
  });
}])

.controller('HomeCtrl', ['$scope', '$location', function($scope, $location) {

//Redirect to the new location regardless of if it has anchor name
   $scope.linkTo = function(id) {
     $location.url(id);
   };

}]);