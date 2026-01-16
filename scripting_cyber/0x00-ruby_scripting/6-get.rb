require 'net/http'
require 'uri'
require 'json'

def get_request(url)
  uri = URI.parse(url)
  response = Net::HTTP.get_response(uri)

  puts "Response status: #{response.code} #{response.message}"
  puts "\nResponse body:\n"

  begin
    json_body = JSON.parse(response.body)
    puts JSON.pretty_generate(json_body)
  rescue JSON::ParserError
    # Əgər JSON deyil, sadəcə çap et
    puts response.body
  end
end
