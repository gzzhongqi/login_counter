class User < ActiveRecord::Base
	validates :name, presence: true,
						 uniqueness: true,
						 length: { maximum: 128 }
	validates :password, length: { maximum: 128 }
	has_secure_password validations: false
end