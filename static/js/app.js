
var registryApp = angular.module('registryApp', []).config(function($interpolateProvider, $httpProvider) {
        $interpolateProvider.startSymbol('{$');
        $interpolateProvider.endSymbol('$}');

        $httpProvider.defaults.xsrfCookieName = 'csrftoken'
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken'
    });;

registryApp.controller('RegistryController', function registryController($scope, $http, $timeout) {

    function digest() {
        if(!$scope.$$phase) {
            $scope.$digest();
        }                      
    }

    function isInteger(string) {
        var digits = new Set(["0","1","2","3","4","5","6","7","8","9"]);
       
        if (string.length === 0) {
            return false;
        }
        
        for (var v of string) {
            if (!digits.has(v)) {
                return false;
            }
        }
        return true;
    }
    
    $scope.account_inputed = false;
    $scope.show_page = false;
    $scope.show_not_found = false;

    $scope.title_style = {'background-color':'#DCE6EF', 'color': '#2B2C34'};
    $scope.title__gas_style = {'color': '#2B2C34'};
    $scope.title__text_style = {'color': 'white'};
    $scope.account__label = {'color': 'red'};
    $scope.account__input_style = {'box-shadow': '0 0 3px #DCE6EF'};
    $scope.user = {};
    $scope.new_phone = "";
    $scope.edit_phone = false;    
    $scope.counter_new = "";
    $scope.payed = false;
    $scope.error = false;
    $scope.error_counter_new = false;
    $scope.error_payed = false;

    function set_error_account_input_color() {
	$scope.account__input_style['border-color']= '#dc746e';
	var input = $('.account__input_style');
	input.style('background-color', '#f8ebeb', 'important');
        digest();
    }


    function get_data() {
	$http({
	  method: 'GET',
	  url: '/get_info',
          params: {account: $scope.ng_account__input}
	}).then(function successCallback(response) {
              console.log(response);
              if (response.statusText === 'OK') {
                  console.log(response);
                  if ('error' in response.data) {
                      $scope.show_not_found = true;
                      set_error_account_input_color();
                  } else {
                      $scope.account__input_style['border-color']= '#61bae9';
                      var input = $('.account__input_style');
                      input.style('background-color', '#e7f1fc', 'important');

                      $scope.user=response.data;
                      $scope.user.counter_new = '';
                      $scope.user.balance_new = $scope.user.indebtedness;
                      if ($scope.user.balance_new.slice(0,1) === '-') {
                          $scope.user.balance_new = '0.0';
                      }
                      if ($scope.user.phone=="") {
                          $scope.phone_is_empty = true;
                      } else {
                          $scope.phone_is_empty = false;
                      }
                      if ($scope.user.email=="") {
                          $scope.email_is_empty = true;
                      } else {
                          $scope.email_is_empty = false;
                      }
                      set_phone_email_color();
                      $scope.show_page = true;
                      digest();
                  }
              } else {
                  $scope.show_page = false;
                  $scope.user={};
                  set_error_account_input_color();
              }
	  }, function errorCallback(response) {
                  $scope.show_page = false;                  
                  $scope.user={};
                  set_error_account_input_color();
	  });
    }

    function set_default_account_input_color() {
        $scope.account__input_style['border-color']= '#DCE6EF';
        var input = $('.account__input_style');
        input.style('background-color', 'white', 'important');
        digest();
    }


    function set_phone_email_color() {
        if (!$scope.phone_is_empty) {
            $scope.phone__text_style = {'background-color': '#e7f1fc'};
            $scope.phone__number_style = {'background-color': '#e7f1fc'};
            $scope.email__text_style = {'background-color': 'white'};
            $scope.email__address_style = {'background-color': 'white'};
        } else {
            if (!$scope.email_is_empty) {
                $scope.email__text_style = {'background-color': '#e7f1fc'};
                $scope.email__address_style = {'background-color': '#e7f1fc'};
            }
        }
    }

    $scope.change = function() {
        if (isInteger($scope.ng_account__input.slice(0,2))) {
            var two_digits = $scope.ng_account__input.slice(0,2);
            var value = parseInt(two_digits, 10);

            // Дагестан
            if (value >= 1 && value <= 59 && two_digits.length === 2) {
                $scope.logo_hash = "dagestan.png";
                $scope.town = "Махачкала";
                $scope.title_style['background-color']='#4A80C1';
                $scope.account_inputed = true;
                set_default_account_input_color();
            } else
                // Северная Осетия
                if (value >= 60 && value <= 66) {
                    $scope.logo_hash = "so.png";
                    $scope.town = "Владикавказ";
                    $scope.title_style['background-color']='#4A80C1';
                    $scope.account_inputed = true;
                    set_default_account_input_color();
                } else 
                    // КБР
                    if (value >= 71 && value <= 82) {
                        $scope.logo_hash = "kbr.png";
                        $scope.town = "Нальчик";
                        $scope.title_style['background-color']='#4A80C1';                        
                        $scope.account_inputed = true;
                        set_default_account_input_color();
                    } else {
                        $scope.title_style['background-color']='#DCE6EF';
                        $scope.title_style['color']= '#2B2C34';                        
                        $scope.account_inputed = false;
                        $scope.show_page = false;
                        set_default_account_input_color();
                    }
   
             if (isInteger($scope.ng_account__input) && $scope.ng_account__input.length===10) {
                if (value>=1 && value<=66 || value>=71 && value<=82) {
                    get_data();                    
                } else {
                    $scope.show_not_found = true;
                    $scope.show_page = false;
                    set_error_account_input_color();
                }
            } else {
                $scope.show_page = false;
                $scope.show_not_found = false;
                if ($scope.ng_account__input.length===10) {
                    $scope.show_not_found = true;
                    set_error_account_input_color();
                } else {
                    set_default_account_input_color();
                }
            }                    
        } else {
            $scope.account_inputed = false;
            $scope.show_page = false;

            if ($scope.ng_account__input.length===10) {
               $scope.show_not_found = true;
               set_error_account_input_color();
            } else {
                $scope.title_style={'background-color':'#DCE6EF', 'color': '#2B2C34'};
                set_default_account_input_color();
            }
        }
    };

    $scope.save_phone = function(){
	$http({
	  method: 'POST',
	  url: '/save_phone/',
          params: {account: $scope.ng_account__input, phone:$scope.user.phone}
	}).then(function successCallback(response) {
              console.log(response);
              if (response.statusText === 'OK') {
                  console.log(response);
                  if ('error' in response.data) {                      
                  } else {
                      $scope.edit_phone = false;
                      if ($scope.user.phone=="") {
                          $scope.phone_is_empty = true;
                      } else {
                          $scope.phone_is_empty = false;
                      }
                      set_phone_email_color();
                      digest();
                  }
              } else {
                  
              }
	  }, function errorCallback(response) {
	  });    
    }

    $scope.save_email = function(){
	$http({
	  method: 'POST',
	  url: '/save_email/',
          params: {account: $scope.ng_account__input, email:$scope.user.email}
	}).then(function successCallback(response) {
              console.log(response);
              if (response.statusText === 'OK') {
                  console.log(response);
                  if ('error' in response.data) {                      
                  } else {
                      $scope.edit_email = false;
                      if ($scope.user.email=="") {
                          $scope.email_is_empty = true;
                      } else {
                          $scope.email_is_empty = false;
                      }
                      set_phone_email_color();
                      digest();
                   }
              } else {
                  
              }
	  }, function errorCallback(response) {
	  });    
    }

    $scope.pay = function() {
        if ($scope.user.is_counter=='0' || isInteger($scope.counter_new)) {
            if ($scope.user.balance_new.match(/^\d+(\.\d+)?$/)) {
		$http({
		  method: 'POST',
		  url: '/pay/',
		  params: {
		      account: $scope.ng_account__input,
		      phone:$scope.user.phone,
		      email:$scope.user.email,
		      balance_new:$scope.user.balance_new,
		      counter_new:$scope.counter_new
		  }
		}).then(function successCallback(response) {
		      console.log(response);
		      if (response.statusText === 'OK') {
		          console.log(response);
		          if ('error' in response.data) {
		              $scope.error = true;
			      $timeout(function() {
				  $scope.error = false;
			      }, 3000);
		          } else {                     
		              $scope.payed = true;
		              $scope.user.balance_new = $scope.user.indebtedness;
		              if ($scope.user.balance_new.slice(0,1) === '-') {
		                  $scope.user.balance_new = '0.0';
		              }
                              $scope.counter_new = "";
		              if ($scope.user.phone=="") {
		                  $scope.phone_is_empty = true;
		              } else {
		                  $scope.phone_is_empty = false;
		              } 
		              if ($scope.user.email=="") {
		                  $scope.email_is_empty = true;
		              } else {
		                  $scope.email_is_empty = false;
		              }
                              set_phone_email_color();
                              digest();
			      $timeout(function() {
				  $scope.payed = false;
			      }, 3000);
		          }
		      } else {
		              $scope.error = true;
			      $timeout(function() {
				  $scope.error = false;
			      }, 3000);
		      }
		  }, function errorCallback(response) {
		              $scope.error = true;
			      $timeout(function() {
				  $scope.error = false;
			      }, 3000);

		  });
            } else {
              $scope.error_payed = true;
	      $timeout(function() {
		  $scope.error_payed = false;
	      }, 3000);
            }
        } else {
              $scope.error_counter_new = true;
	      $timeout(function() {
		  $scope.error_counter_new = false;
	      }, 3000);

           if (!$scope.user.balance_new.match(/^\d+(\.\d+)?$/)) {
              $scope.error_payed = true;
	      $timeout(function() {
		  $scope.error_payed = false;
	      }, 3000);               
           }
        }
    }
});

(function($) {    
  if ($.fn.style) {
    return;
  }

  // Escape regex chars with \
  var escape = function(text) {
    return text.replace(/[-[\]{}()*+?.,\\^$|#\s]/g, "\\$&");
  };

  // For those who need them (< IE 9), add support for CSS functions
  var isStyleFuncSupported = !!CSSStyleDeclaration.prototype.getPropertyValue;
  if (!isStyleFuncSupported) {
    CSSStyleDeclaration.prototype.getPropertyValue = function(a) {
      return this.getAttribute(a);
    };
    CSSStyleDeclaration.prototype.setProperty = function(styleName, value, priority) {
      this.setAttribute(styleName, value);
      var priority = typeof priority != 'undefined' ? priority : '';
      if (priority != '') {
        // Add priority manually
        var rule = new RegExp(escape(styleName) + '\\s*:\\s*' + escape(value) +
            '(\\s*;)?', 'gmi');
        this.cssText =
            this.cssText.replace(rule, styleName + ': ' + value + ' !' + priority + ';');
      }
    };
    CSSStyleDeclaration.prototype.removeProperty = function(a) {
      return this.removeAttribute(a);
    };
    CSSStyleDeclaration.prototype.getPropertyPriority = function(styleName) {
      var rule = new RegExp(escape(styleName) + '\\s*:\\s*[^\\s]*\\s*!important(\\s*;)?',
          'gmi');
      return rule.test(this.cssText) ? 'important' : '';
    }
  }

  // The style function
  $.fn.style = function(styleName, value, priority) {
    // DOM node
    var node = this.get(0);
    // Ensure we have a DOM node
    if (typeof node == 'undefined') {
      return this;
    }
    // CSSStyleDeclaration
    var style = this.get(0).style;
    // Getter/Setter
    if (typeof styleName != 'undefined') {
      if (typeof value != 'undefined') {
        // Set style property
        priority = typeof priority != 'undefined' ? priority : '';
        style.setProperty(styleName, value, priority);
        return this;
      } else {
        // Get style property
        return style.getPropertyValue(styleName);
      }
    } else {
      // Get CSSStyleDeclaration
      return style;
    }
  };
})(jQuery);
