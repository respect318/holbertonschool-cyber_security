require 'net/http'
require 'uri'
require 'json'

def get_request(url)
  uri = URI(url)
  response = Net::HTTP.get_response(uri)

  # Status
  print "Response status: #{response.code} #{response.message}\n"

  # Body
  print "\nResponse body:\n\n"

  begin
    json_body = JSON.parse(response.body)
    print JSON.pretty_generate(json_body)
  rescue JSON::ParserError
    print response.body
  end
end
