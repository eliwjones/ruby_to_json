#!/usr/bin/env ruby

require 'json'
begin
  result = eval(ARGV[0])
rescue Exception => result
  # Exception passed back in result so can more readily be seen by wrapper.
end
print result.to_json
