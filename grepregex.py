import sublime
import sublime_plugin
import re

class GrepRegExCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sublime.active_window().show_input_panel("Regex search string:", "", self.on_Search_String, None, None)
		pass
	def on_Search_String(self, user_input):
		try:
			if sublime.active_window():
				sublime.active_window().run_command("grep_reg_ex_engine", {"query": user_input} )
		except ValueError as e:
			sublime.status_message(e)

class GrepRegExEngineCommand(sublime_plugin.TextCommand):
	def run(self, edit, query):
		self.window = sublime.active_window()
		if not query:
			self.window.status_message("Nothing to search for.")
		else:
			allcontent = sublime.Region(0, self.view.size())
			if allcontent.empty():
				self.window.status_message("No content to search.")
			else:
				self.window.status_message("Searching for " + query)
				newView = sublime.active_window().new_file()
				for line in self.view.lines(allcontent):
					s = self.view.substr(line) + "\n"
					if re.search(query,s):
						newView.insert(edit, newView.sel()[0].begin(), s)
