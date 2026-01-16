require 'open-uri'
require 'fileutils'

# Check for arguments
if ARGV.length != 2
  puts "Usage: 9-download_file.rb URL LOCALFILE_PATH"
  exit
end

url = ARGV[0]
local_path = ARGV[1]

puts "Downloading file from #{url}…"

# Create folder if not exists
dir = File.dirname(local_path)
FileUtils.mkdir_p(dir) unless Dir.exist?(dir)

# Download and save
URI.open(url) do |remote_file|
  File.open(local_path, "wb") do |file|
    file.write(remote_file.read)
  end
end

puts "File downloaded and saved to #{local_path}."
