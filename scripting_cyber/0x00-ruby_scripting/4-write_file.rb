require 'json'

def merge_json_files(file1_path, file2_path)
  json1 = JSON.parse(File.read(file1_path))
  json2 = JSON.parse(File.read(file2_path))

  merged = json2 + json1

  File.open(file2_path, 'w') do |f|
    f.write(JSON.pretty_generate(merged))
  end

  puts "Merged JSON written to #{file2_path}"
end
