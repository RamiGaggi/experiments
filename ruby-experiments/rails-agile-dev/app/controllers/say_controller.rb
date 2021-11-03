# frozen_string_literal: true

class SayController < ApplicationController
  def hello
    @time = Time.know
  end

  def goodbye; end\
end
