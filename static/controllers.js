angular.module("howdoibeat", ['ngCookies'])

.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[');
  $interpolateProvider.endSymbol(']}');
})

.run (function ($rootScope, $http, $cookies, $cookieStore, $location){
 
})

.controller("IndexController", function($scope, $rootScope, $http) {
    $scope.page = {};
    $scope.page.firstname = 'hi';
    $rootScope.address = '';
    $scope.beatdata = {};
    $scope.summoner={};
    $scope.loading = false;
    $scope.loaded = false;
    $scope.fetchdata = function(){
      $scope.loading = true;
        $http.post ('/'+$scope.summoner.name, {}).
          success(function(data, status, headers, config) {
            // this callback will be called asynchronously
            // when the response is available
            console.log(data);
            console.log (status);
            //$cookieStore.put ('uid', data.pid);
            //$cookieStore.put ('oid', data.oid);
            //window.location.href = $rootScope.url+'dash.html'
            $scope.beatdata = data;
            $scope.loaded = true;
            $scope.loading = false;
            //console.log ($scope.beatdata[0].championId);
          }).
          error(function(data, status, headers, config) {
            // called asynchronously if an error occurs
            // or server returns response with an error status.
            console.log(data);
            console.log (status);
            $scope.loading = false;
          });
    }
    //$scope.fetchdata('leotam1234');
});