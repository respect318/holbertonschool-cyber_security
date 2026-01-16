require 'open-uri'
require 'uri'
require 'fileutils'

def download_file(url, local_path)
    if url.nil? || local_path.nil?
        puts "Usage: 9-download_file.rb URL LOCAL_FILE_PATH"
        return
    end

    FileUtils.mkdir_p(File.dirname(local_path))
    puts "Downloading file from #{url}..."
    URI.open(url) do |file|
        File.open(local_path, 'wb') do |out_file|
            out_file.write(file.read)
        end
    end
    puts "File downloaded and saved to #{local_path}"
end

if ARGV.length != 2
    puts "Usage: 9-download_file.rb URL LOCAL_FILE_PATH"
else
    url = ARGV[0]
    local_path = ARGV[1]
    download_file(url, local_path)
end
