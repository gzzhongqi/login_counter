Counter::Application.routes.draw do

  resources :users, :defaults => { :format => "json" }

  match '/users/login', to: 'users#login', via: :post
  match '/users/add',   to: 'users#add',   via: :post
  match '/TESTAPI/resetFixture', to: 'users#reset', via: :post
  match '/TESTAPI/unitTests',    to: 'users#tests', via: :post


end
