require 'net/http'
require 'uri'
require 'json'

def post_request(url, body_params)
  uri = URI(url)

  http = Net::HTTP.new(uri.host, uri.port)
  http.use_ssl = (uri.scheme == "https")

  request = Net::HTTP::Post.new(uri.path, { 'Content-Type' => 'application/json' })
  request.body = body_params.to_json

  response = http.request(request)

  # Status
  print "Response status: #{response.code} #{response.message}\n\n"

  # Body
  print "Response body:\n\n"

  begin
    json_body = JSON.parse(response.body)
    print JSON.pretty_generate(json_body)
  rescue JSON::ParserError
    print response.body
  end
end
