require 'spec_helper'

describe "UnitTests" do
	before do
		@user = User.new(name: "user_test", password: "password", password_confirmation: "password")
	end

	subject{@user}

	it {should respond_to(:name)}
	it {should respond_to(:password)}
	it {should respond_to(:password_digest)}
	it {should respond_to(:counter)}

	describe "password can be empty" do
		before {@user.password = ""}
		it {should be_valid}
	end

	describe "password can't be too long" do
		before {@user.password = "a"*129}
		it {should_not be_valid}
	end

	describe "name can't be too long" do 
		before {@user.name = "a"*129}
		it {should_not be_valid}
	end

	describe "name can't be blank" do 
		before {@user.name = ""}
		it {should_not be_valid}
	end

	describe "common names is valid" do 
		before {@user.name = "adsds"}
		it {should be_valid}
	end

	describe "name must be unique" do 
		before {
			User.create(name: "user_test", password: "pass", password_confirmation: "pass")
		}
		it {should_not be_valid}
	end

	after(:each) do
  		User.delete_all
	end
end
