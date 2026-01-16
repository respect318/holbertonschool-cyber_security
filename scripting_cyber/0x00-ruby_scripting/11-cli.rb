#!/usr/bin/env ruby
require 'optparse'

# Define the file where tasks will be stored
TASK_FILE = "tasks.txt"

# Ensure the file exists so read operations don't fail
File.open(TASK_FILE, 'a') {}

options = {}

opt_parser = OptionParser.new do |opts|
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
end

# Parse the command line arguments
begin
  opt_parser.parse!
rescue OptionParser::InvalidOption, OptionParser::MissingArgument => e
  puts e.message
  puts opt_parser
  exit 1
end

# Logic for Adding a Task
if options[:add]
  File.open(TASK_FILE, "a") do |f|
    f.puts options[:add]
  end
  puts "Task '#{options[:add]}' added."
end

# Logic for Listing Tasks
if options[:list]
  tasks = File.readlines(TASK_FILE)
  if tasks.empty?
    puts "No tasks found."
  else
    puts tasks.map(&:strip)
  end
end

# Logic for Removing a Task
if options[:remove]
  tasks = File.readlines(TASK_FILE)
  index = options[:remove] - 1 # Convert to 0-based index

  if index >= 0 && index < tasks.length
    removed_task = tasks.delete_at(index).strip
    File.open(TASK_FILE, "w") do |f|
      f.puts tasks
    end
    puts "Task '#{removed_task}' removed."
  else
    puts "Error: Task at index #{options[:remove]} not found."
  end
end
