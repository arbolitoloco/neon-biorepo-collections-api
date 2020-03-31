require 'csv'
require 'json'
require 'cgi'

DATA_FILES = %w(
    data/categories.csv
)

BUILD_DIR = 'build/'

class Record
    attr_reader :row

    def initialize(row)
        @row = row
    end

end

class APIWriter
    def write_index(collection)
        IO.write(File.join(BUILD_DIR, 'index.json'), collection + "\n")
    end

    def write_item(item, acronym)
        dirname = CGI.escape(acronym)
        Dir.mkdir(File.join(BUILD_DIR, dirname))
        IO.write(File.join(BUILD_DIR, dirname, 'index.json'), item + "\n")
    end
end

writer = APIWriter.new
data = |row| Record.new(row) }.sort_by(&:acronym).group_by(&:acronym)
data.transform_values! { |records| records.map(&:to_h) }

collection = data.dup

writer.write_index(JSON.pretty_generate(collection))
data.each do |key, records|
    item = {
        key => records
    }
    writer.write_item(JSON.pretty_generate(item), key)
end
