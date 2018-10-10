# Freeze Ruby Files

This Sublime 3 plugin automatically adds the [magic comment introduced in Ruby
2.3](https://www.lucascaton.com.br/2016/01/19/what-is-frozen_string_literal-in-ruby/)
to all your Ruby files when saving them.

It checks the Ruby version (by running `ruby -v` in the file's folder) in order
to only add the magic comment in Ruby files where Ruby version > 2.3.
