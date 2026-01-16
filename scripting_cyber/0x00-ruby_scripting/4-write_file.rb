require 'json'

def merge_json_files(file1_path, file2_path)
  # file1 -> əlavə ediləcək
  # file2 -> əsas fayl

  data1 = JSON.parse(File.read(file1_path))
  data2 = JSON.parse(File.read(file2_path))

  merged = data2 + data1

  File.open(file2_path, 'w') do |file|
    file.write(JSON.pretty_generate(merged))
  end
end
