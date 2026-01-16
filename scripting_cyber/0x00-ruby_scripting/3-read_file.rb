require 'json'

def count_user_ids(path)
  # 1. Faylı oxu
  file_content = File.read(path)

  # 2. JSON-u Ruby obyektinə çevir
  data = JSON.parse(file_content)

  # 3. userId-ləri saymaq üçün hash
  counts = Hash.new(0)

  # 4. Hər element üzrə userId say
  data.each do |item|
    user_id = item["userId"]
    counts[user_id] += 1
  end

  # 5. Nəticəni çap et
  counts.each do |user_id, count|
    puts "#{user_id}: #{count}"
  end
end
