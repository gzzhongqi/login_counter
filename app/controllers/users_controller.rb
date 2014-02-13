class UsersController < ApplicationController


  def login
  	@user = User.find_by_name(params[:user])
  	if @user != nil && @user.authenticate(params[:password])
  		@user.counter += 1
  		@user.save
  		render :json => {
  			count: @user.counter, 
  			errCode: 1
  		}
  	else
  		render :json => {
  			errCode: -1
  		}

  	end
  end

  def add
  	if User.find_by_name(params[:user]) != nil
  		render :json => {
  			errCode: -2
  		}
  	else
  		if params[:user] == nil or params[:user].length > 128 or params[:user] == ""
  			render :json => {
  				errCode: -3
  			}
  		elsif params[:password].length > 128
  			render :json => {
  				errCode: -4
  			}
  		else
  			@user = User.create(name: params[:user], password: params[:password], password_confirmation: params[:password], counter: 1)
  			render :json => {
  				count: @user.counter, 
  				errCode: 1
  			}
  		end	
  	end
  end

  def reset
  	User.destroy_all()
	render :json => { errCode: 1 }
  end

  def tests
  	result_old = `rspec`
	result  = result_old.split(" ")
	total_test = result[result.index("examples,") - 1]
	failures   = result[result.index("failures") - 1]

	render :json => { nrFailed: failures.to_i,
					  output: result_old,
					  totalTests: total_test.to_i }
  end


end
