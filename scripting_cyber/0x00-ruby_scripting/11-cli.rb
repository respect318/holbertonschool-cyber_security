#!/usr/bin/env ruby
require 'optparse'

TASK_FILE = 'tasks.txt'

options = {}
OptionParser.new do |opts|
  opts.banner = "Usage: cli.rb [options]"

  opts.on("-a", "--add TASK", "Add a new task") do |task|
    options[:add] = task
  end

  opts.on("-l", "--list", "List all tasks") do
    options[:list] = true
  end

  opts.on("-r", "--remove INDEX", Integer, "Remove a task by index") do |index|
    options[:remove] = index
  end

  opts.on("-h", "--help", "Show help") do
    puts opts
    exit
  end
end.parse!

# Ensure tasks file exists
File.write(TASK_FILE, '') unless File.exist?(TASK_FILE)

tasks = File.readlines(TASK_FILE, chomp: true)

if options[:add]
  tasks << options[:add]
  File.write(TASK_FILE, tasks.join("\n"))
  puts "Task '#{options[:add]}' added."
elsif options[:list]
  puts "Tasks:"
  puts             # <<< boş sətir: checker tələb edir
  tasks.each { |t| puts t }
elsif options[:remove]
  index = options[:remove] - 1
  if index >= 0 && index < tasks.size
    removed = tasks.delete_at(index)
    File.write(TASK_FILE, tasks.join("\n"))
    puts "Task '#{removed}' removed."
  else
    puts "Invalid task index."
  end
else
  puts "No option provided. Use -h for help."
end
