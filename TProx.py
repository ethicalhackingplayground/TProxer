from burp import IBurpExtender, IScanIssue, IScannerCheck, IContextMenuFactory, ITab
from javax.swing import JMenuItem, JFileChooser
from java.awt import Font
from javax.swing import JPanel, JButton, JTable, table, JLabel, JScrollPane, JTextField, GroupLayout, LayoutStyle, JFrame
import java.util.ArrayList as ArrayList
import java.lang.String as String
from java.lang import Short

import thread

queryPayloadsFile = open('query payloads.txt', "r")
queryPayloadsFromFile = queryPayloadsFile.readlines()

wordlistTest=[]
extentionName = "TProxer"
requestNum = 2

# The Burp Tab UI
class uiTab(JFrame):

	# Load a wordlist used for content discovery.
	def wordlistAddButtonClicked(self, event):
		wordlistData = []
		self.filechooser = JFileChooser("")
		self.filechooser.setFileSelectionMode(JFileChooser.FILES_ONLY)
		selected = self.filechooser.showSaveDialog(None)
		if selected == JFileChooser.APPROVE_OPTION:
			file = self.filechooser.getSelectedFile()
			wordlist = open(file.getAbsolutePath(), 'r').readlines()
			for word in wordlist:
				wordlistTest.append(word.strip())
				wordlistData.append([word])
				self.wordlistTableColumns = [None]
				self.wordlistTableModel = table.DefaultTableModel(wordlistData,self.wordlistTableColumns)
				self.wordlistTable.setModel(self.wordlistTableModel)
				self.wordlistTable.getTableHeader().setUI(None)
				self.jScrollPane2.setViewportView(self.wordlistTable)

	# The button to Add the traversal payloads.
	def queryAddButtonClicked(self, event):
		textFieldValue = self.queryPayloadsAddPayloadTextField.getText()

		if textFieldValue != "":
			tableModel = self.queryPayloadsTable.getModel()
			tableModel.addRow([textFieldValue])
		self.queryPayloadsAddPayloadTextField.setText("")

	# The button to clear the payloads.
	def queryClearButtonClicked(self, event):
		global requestNum
		requestNum = 2
		tableModel = self.queryPayloadsTable.getModel()
		tableModel.setRowCount(0)

	# The button to remove a single payload.
	def queryRemoveButtonClicked(self, event):
		tableModel = self.queryPayloadsTable.getModel()
		selectedRows = self.queryPayloadsTable.getSelectedRows()
		for row in selectedRows:
			tableModel.removeRow(row)
		global requestNum
		if requestNum > 2:
			requestNum -= 1
			
	# The button to clear the wordlist.
	def wordlistClearButtonClicked(self, event):
		global requestNum
		requestNum = 2
		tableModel = self.wordlistTable.getModel()
		tableModel.setRowCount(0)

	# The button to remove a single wordlist item.
	def wordlistRemoveButtonClicked(self, event):
		tableModel = self.wordlistTable.getModel()
		selectedRows = self.wordlistTable.getSelectedRows()
		for row in selectedRows:
			tableModel.removeRow(row)
		global requestNum
		if requestNum > 2:
			requestNum -= 1

	# Contructor 
	def __init__(self):
		self.queryPayloadsLabel = JLabel()
		self.jScrollPane1 = JScrollPane()
		self.queryPayloadsTable = JTable()
		self.queryPayloadsAddPayloadTextField = JTextField()
		self.queryPayloadsAddButton = JButton("Add", actionPerformed=self.queryAddButtonClicked)
		self.queryPayloadsClearButton = JButton("Clear", actionPerformed=self.queryClearButtonClicked)
		self.queryPayloadsRemoveButton = JButton("Remove", actionPerformed=self.queryRemoveButtonClicked)

		self.wordlistLabel = JLabel()
		self.jScrollPane2 = JScrollPane()
		self.wordlistTable = JTable()
		self.wordlistTextField = JTextField()
		self.wordlistAddButton = JButton("Choose", actionPerformed=self.wordlistAddButtonClicked)
		self.wordlistClearButton = JButton("Clear", actionPerformed=self.wordlistClearButtonClicked)
		self.wordlistRemoveButton = JButton("Remove", actionPerformed=self.wordlistRemoveButtonClicked)
		self.panel = JPanel()

		self.wordlistLabel.setText("Wordlist")

		self.queryPayloadsLabel.setText("Traversal Payloads")

		queryTableData = []
		for queryPayload in queryPayloadsFromFile:
			queryTableData.append([queryPayload])


		queryTableColumns = [None]
		queryTableModel = table.DefaultTableModel(queryTableData,queryTableColumns)
		self.queryPayloadsTable.setModel(queryTableModel)
		self.queryPayloadsTable.getTableHeader().setUI(None)

		self.jScrollPane1.setViewportView(self.queryPayloadsTable)


		layout = GroupLayout(self.panel)
		self.panel.setLayout(layout)

		layout.setHorizontalGroup(
			layout.createParallelGroup(GroupLayout.Alignment.LEADING)
			.addGroup(layout.createSequentialGroup()
				.addGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING, False)
					.addComponent(self.queryPayloadsAddButton, GroupLayout.DEFAULT_SIZE, GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
					.addComponent(self.queryPayloadsRemoveButton, GroupLayout.DEFAULT_SIZE, GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
					.addComponent(self.queryPayloadsClearButton, GroupLayout.PREFERRED_SIZE, 93, GroupLayout.PREFERRED_SIZE))
				.addPreferredGap(LayoutStyle.ComponentPlacement.RELATED)
				.addGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING, False)
					.addComponent(self.queryPayloadsLabel)
					.addComponent(self.queryPayloadsAddPayloadTextField)
					.addComponent(self.jScrollPane1, GroupLayout.PREFERRED_SIZE, 107, GroupLayout.PREFERRED_SIZE))
				.addGap(100, 100, 100)
				.addGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING, False)
					.addComponent(self.wordlistAddButton, GroupLayout.DEFAULT_SIZE, GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
					.addComponent(self.wordlistRemoveButton, GroupLayout.DEFAULT_SIZE, GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
					.addComponent(self.wordlistClearButton, GroupLayout.PREFERRED_SIZE, 93, GroupLayout.PREFERRED_SIZE))
				.addPreferredGap(LayoutStyle.ComponentPlacement.RELATED)
				.addGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING, False)
					.addComponent(self.wordlistLabel)
					.addComponent(self.wordlistTextField)
					.addComponent(self.jScrollPane2, GroupLayout.PREFERRED_SIZE, 107, GroupLayout.PREFERRED_SIZE))
				.addGap(0, 483, Short.MAX_VALUE))
		)
		layout.setVerticalGroup(
			layout.createParallelGroup(GroupLayout.Alignment.LEADING)
			.addGroup(layout.createSequentialGroup()
				.addGap(17, 17, 17)
				.addGroup(layout.createParallelGroup(GroupLayout.Alignment.TRAILING)
					.addGroup(layout.createSequentialGroup()
						.addComponent(self.wordlistLabel)
						.addPreferredGap(LayoutStyle.ComponentPlacement.RELATED)
						.addGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING)
							.addComponent(self.jScrollPane2, GroupLayout.PREFERRED_SIZE, 195, GroupLayout.PREFERRED_SIZE)
							.addGroup(layout.createSequentialGroup()
								.addComponent(self.wordlistClearButton)
								.addPreferredGap(LayoutStyle.ComponentPlacement.RELATED)
								.addComponent(self.wordlistRemoveButton)))
						.addPreferredGap(LayoutStyle.ComponentPlacement.RELATED)
						.addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
							.addComponent(self.wordlistTextField, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)
							.addComponent(self.wordlistAddButton)))
					.addGroup(layout.createSequentialGroup()
						.addComponent(self.queryPayloadsLabel)
						.addPreferredGap(LayoutStyle.ComponentPlacement.RELATED)
						.addGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING)
							.addComponent(self.jScrollPane1, GroupLayout.PREFERRED_SIZE, 195, GroupLayout.PREFERRED_SIZE)
							.addGroup(layout.createSequentialGroup()
								.addComponent(self.queryPayloadsClearButton)
								.addPreferredGap(LayoutStyle.ComponentPlacement.RELATED)
								.addComponent(self.queryPayloadsRemoveButton)))
						.addPreferredGap(LayoutStyle.ComponentPlacement.RELATED)
						.addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
							.addComponent(self.queryPayloadsAddPayloadTextField, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)
							.addComponent(self.queryPayloadsAddButton))))
				.addContainerGap(324, Short.MAX_VALUE))
		)


# The class to extend Burps functionalities
class BurpExtender(IBurpExtender, IScannerCheck, IContextMenuFactory, ITab):

	# We define our initial variables in this callback function.
	def registerExtenderCallbacks(self, callbacks):
		self.callbacks = callbacks
		self.helpers = self.callbacks.getHelpers()
		self.callbacks.registerScannerCheck(self)
		self.callbacks.registerContextMenuFactory(self)
		self.callbacks.setExtensionName(extentionName)

		self.callbacks.addSuiteTab(self)

		sys.stdout = self.callbacks.getStdout()
		sys.stderr = self.callbacks.getStderr()
		
		return None

	# The extension name.
	def getTabCaption(self):
		return extentionName

	# The Ui component.
	def getUiComponent(self):
		self.frm = uiTab()
		return self.frm.panel

	# Setup the menu items.
	def createMenuItems(self, invocation):
		self.context = invocation
		self.menuList = []
		self.menuItem = JMenuItem("TProxer", actionPerformed=self.testFromMenu)
		self.menuList.append(self.menuItem)
		return self.menuList

	# Perform the active scan.
	def testFromMenu(self, event):
		selectedMessages = self.context.getSelectedMessages()
		for message in selectedMessages:
			thread.start_new_thread(self.doActiveScan, (message, "" , True, ))
		return None


	# Validate if the file/directory is internal
	def isInternal(self, httpService, word, request, requestPath):

		publicPathTest = ""
		if requestPath.endswith("/"):
			publicPathTest = requestPath + word
		else:
			publicPathTest = requestPath + "/" + word
		originalRequest = self.helpers.bytesToString(request.getRequest())
		newVulnUrl = originalRequest.replace(requestPath, publicPathTest)
		newVulnRequest = self.callbacks.makeHttpRequest(httpService, newVulnUrl)
		newVulnRequestStatus = str(self.helpers.analyzeResponse(newVulnRequest.getResponse()).getStatusCode())
		if newVulnRequestStatus != "200":
			return newVulnUrl
		else:
			return None

	
	# Generate the traversal payload scenerios
	def generateTraversal(self, path, payload, statusTestCase):

		# Generate the 400 test scenerios
		if statusTestCase == "400":
			finalPayload=""
			slashes = path.split('/')
			numSlashes = len(slashes)-1
			for _ in range(0,numSlashes+5):
				finalPayload = finalPayload + payload + "/"

		# Generate the 404 test scenerios
		else:
			finalPayload=""
			slashes = path.split('/')
			numSlashes = len(slashes)-1
			for _ in range(1,numSlashes):
				finalPayload = finalPayload + payload + "/"
		
		# Additional path checks for the final traversal payload
		if (path.endswith("/")):
			return path + finalPayload
		else:
			return path + "/" + finalPayload


	# Attempt to find reverse proxy path based SSRF in the request.
	def tryTestForPathBasedSSRF(self, request, payload, httpService):
		results = []
		#each result element is an array of [detail,httpMessage]

		requestPath = request.getUrl().getPath()
		traversal400 = self.generateTraversal(requestPath, payload, "400")
		
		originalRequest = self.helpers.bytesToString(request.getRequest())
		newRequest400 = originalRequest.replace(requestPath, traversal400)
		newRequestResult400 = self.callbacks.makeHttpRequest(httpService, newRequest400)
		newRequestStatusCode400 = str(self.helpers.analyzeResponse(newRequestResult400.getResponse()).getStatusCode())


		# There may be a proxy in place
		if newRequestStatusCode400 == "400":
			traversal404 = self.generateTraversal(requestPath, payload, "404")
			originalRequest = self.helpers.bytesToString(request.getRequest())
			newRequest404 = originalRequest.replace(requestPath, traversal404)
			newRequestResult404 = self.callbacks.makeHttpRequest(httpService, newRequest404)
			newRequestStatusCode404 = str(self.helpers.analyzeResponse(newRequestResult404.getResponse()).getStatusCode())

			# Testing for any internal files/directorys
			if newRequestStatusCode404 == "404":
				for word in wordlistTest:
					word = word.strip()
					pathtoTest = traversal404 + word
					#print("Testing: " + pathtoTest)
					originalRequest = self.helpers.bytesToString(request.getRequest())
					newRequestTest = originalRequest.replace(requestPath, pathtoTest)
					newRequestTestResult = self.callbacks.makeHttpRequest(httpService, newRequestTest)
					newRequestTestResultStatus = str(self.helpers.analyzeResponse(newRequestTestResult.getResponse()).getStatusCode())
						
					# Check to see if the asset is 100% internal
					if newRequestTestResultStatus == "200":
						discoveredResult = self.isInternal(httpService, word, request, requestPath)
						if discoveredResult != None:
							url = request.getUrl()
							finalExploit = url.getProtocol() + "://" + url.getHost() + pathtoTest
							print("FOUND: "+newRequestTest)
							issue = []
							issue.append("<tr><td><a href='" + str(finalExploit) + "'>"+str(finalExploit)+"</a></td></tr>")
							issue.append(newRequestTestResult)
							results.append(issue)

				#  Return the results
				if len(results) > 0:
					return results
				else:
					return None

	# Latest version of burp does both active and passive scans simultaneously.
	def doPassiveScan(self, baseRequestResponse):
		return None

	# Perform an active scan.
	def doActiveScan(self, baseRequestResponse, insertionPoint, isCalledFromMenu=False):
		result = self.testRequest(baseRequestResponse)
		if result != None:
			if isCalledFromMenu == True:
				self.callbacks.addScanIssue(result[0])
			else:
				return result
		else:
			return None

	# Perform the path traversal tests.
	def testRequest(self, baseRequestResponse):
		queryPayloadsResults = []
		httpService = baseRequestResponse.getHttpService()

		# Store the payloads from the table into an array
		queryPayloadsFromTable = []
		for rowIndex in range(self.frm.queryPayloadsTable.getRowCount()):
			queryPayloadsFromTable.append(str(self.frm.queryPayloadsTable.getValueAt(rowIndex, 0)))

		# Test for path based SSRF in the request
		for payload in queryPayloadsFromTable:
			payload = payload.rstrip('\n')
			result = self.tryTestForPathBasedSSRF(baseRequestResponse, payload, httpService)
			if result != None:
				queryPayloadsResults += result

		# Display the scan issues.
		if len(queryPayloadsResults) > 0:
			issueDetails = []
			issueHttpMessages = []
			issueHttpMessages.append(baseRequestResponse)

			for issue in queryPayloadsResults:
				issueDetails.append(issue[0])
				issueHttpMessages.append(issue[1])

			return [CustomScanIssue(
				httpService,
				self.helpers.analyzeRequest(baseRequestResponse).getUrl(),
				issueHttpMessages,
				"Path Based SSRF Internal Access",
				"<table>" + "".join(issueDetails) + "</table>",
				"High",
				)]
		return None

	# Avoid getting duplicate requests.
	def consolidateDuplicateIssues(self, existingIssue, newIssue):
		if (existingIssue.getIssueDetail() == newIssue.getIssueDetail()):
			return -1
		else:
			return 0

# The CustomScan issue class which defines the scan results.
class CustomScanIssue (IScanIssue):
	def __init__(self, httpService, url, httpMessages, name, detail, severity):
		self._httpService = httpService
		self._url = url
		self._httpMessages = httpMessages
		self._name = name
		self._detail = detail
		self._severity = severity

	def getUrl(self):
		return self._url

	def getIssueName(self):
		return self._name

	def getIssueType(self):
		return 0

	def getSeverity(self):
		return self._severity

	def getConfidence(self):
		return "Certain"

	def getIssueBackground(self):
		return extentionName + " sent a request and got 400 Bad Request Response. " + extentionName + " sent another request then got a 404 Not Found response, then found a potential backend asset through content discovery, this may indicate a misconfiguration on the server side that allows access to internal assests through a path based SSRF attack."

	def getRemediationBackground(self):
		return  extentionName + " Suggests that you fix up your reverse proxy rules to disallow traversal attacks through correct regex patterns. For some additional advice would be to also implement a Web Application Firewall to further increase the security tightness."

	def getIssueDetail(self):
		return self._detail
	def getRemediationDetail(self):
		pass

	def getHttpMessages(self):
		return self._httpMessages

	def getHttpService(self):
		return self._httpService
