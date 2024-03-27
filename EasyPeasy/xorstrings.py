{"payload":{"allShortcutsEnabled":false,"fileTree":{"":{"items":[{"name":"LICENSE.txt","path":"LICENSE.txt","contentType":"file"},{"name":"README.md","path":"README.md","contentType":"file"},{"name":"cribdrag.py","path":"cribdrag.py","contentType":"file"},{"name":"samples.txt","path":"samples.txt","contentType":"file"},{"name":"xorstrings.py","path":"xorstrings.py","contentType":"file"}],"totalCount":5}},"fileTreeProcessingTime":1.1589479999999999,"foldersToFetch":[],"repo":{"id":12025016,"defaultBranch":"master","name":"cribdrag","ownerLogin":"SpiderLabs","currentUserCanPush":false,"isFork":false,"isEmpty":false,"createdAt":"2013-08-10T18:31:21.000Z","ownerAvatar":"https://avatars.githubusercontent.com/u/508521?v=4","public":true,"private":false,"isOrgOwned":true},"symbolsExpanded":false,"treeExpanded":true,"refInfo":{"name":"master","listCacheKey":"v0:1376159545.0","canEdit":false,"refType":"branch","currentOid":"2d27dbf2e18f986b5bbc3fcb6851783e88f13b1b"},"path":"xorstrings.py","currentUser":null,"blob":{"rawLines":["#!/usr/bin/python","","##########################","# cribdrag - An interactive crib dragging tool","# Daniel Crowley","# Copyright (C) 2013 Trustwave Holdings, Inc.","# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.","# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.","# You should have received a copy of the GNU General Public License along with this program. If not, see <http://www.gnu.org/licenses/>.","##########################","","import sys","import argparse","","def sxor(s1,s2):    ","    # convert strings to a list of character pair tuples","    # go through each tuple, converting them to ASCII code (ord)","    # perform exclusive or on the ASCII code","    # then convert the result back to ASCII (chr)","    # merge the resulting array of characters as a string","    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))","","parser = argparse.ArgumentParser(description='xorstrings is a utility which comes with cribdrag, the interactive crib dragging tool. xorstrings takes two ASCII hex encoded strings and XORs them together. This can be useful when cryptanalyzing ciphertext produced by the One Time Pad algorithm or a stream cipher when keys are reused, as one can XOR two ciphertexts together and then crib drag across the result, which is both plaintexts XORed together.')","parser.add_argument('data1', help='Data encoded in an ASCII hex format (ie. ABC would be 414243)')","parser.add_argument('data2', help='Data encoded in an ASCII hex format (ie. ABC would be 414243)')","args = parser.parse_args()","","s1 = args.data1.decode('hex')","s2 = args.data2.decode('hex')","","s3 = sxor(s1, s2)","","print s3.encode('hex')"],"stylingDirectives":[[{"start":0,"end":17,"cssClass":"pl-c"}],[],[{"start":0,"end":26,"cssClass":"pl-c"}],[{"start":0,"end":46,"cssClass":"pl-c"}],[{"start":0,"end":16,"cssClass":"pl-c"}],[{"start":0,"end":45,"cssClass":"pl-c"}],[{"start":0,"end":241,"cssClass":"pl-c"}],[{"start":0,"end":234,"cssClass":"pl-c"}],[{"start":0,"end":136,"cssClass":"pl-c"}],[{"start":0,"end":26,"cssClass":"pl-c"}],[],[{"start":0,"end":6,"cssClass":"pl-k"},{"start":7,"end":10,"cssClass":"pl-s1"}],[{"start":0,"end":6,"cssClass":"pl-k"},{"start":7,"end":15,"cssClass":"pl-s1"}],[],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":8,"cssClass":"pl-en"},{"start":9,"end":11,"cssClass":"pl-s1"},{"start":12,"end":14,"cssClass":"pl-s1"}],[{"start":4,"end":56,"cssClass":"pl-c"}],[{"start":4,"end":64,"cssClass":"pl-c"}],[{"start":4,"end":44,"cssClass":"pl-c"}],[{"start":4,"end":49,"cssClass":"pl-c"}],[{"start":4,"end":57,"cssClass":"pl-c"}],[{"start":4,"end":10,"cssClass":"pl-k"},{"start":11,"end":13,"cssClass":"pl-s"},{"start":14,"end":18,"cssClass":"pl-en"},{"start":19,"end":22,"cssClass":"pl-en"},{"start":23,"end":26,"cssClass":"pl-en"},{"start":27,"end":28,"cssClass":"pl-s1"},{"start":30,"end":31,"cssClass":"pl-c1"},{"start":32,"end":35,"cssClass":"pl-en"},{"start":36,"end":37,"cssClass":"pl-s1"},{"start":40,"end":43,"cssClass":"pl-k"},{"start":44,"end":45,"cssClass":"pl-s1"},{"start":46,"end":47,"cssClass":"pl-s1"},{"start":48,"end":50,"cssClass":"pl-c1"},{"start":51,"end":54,"cssClass":"pl-en"},{"start":55,"end":57,"cssClass":"pl-s1"},{"start":58,"end":60,"cssClass":"pl-s1"}],[],[{"start":0,"end":6,"cssClass":"pl-s1"},{"start":7,"end":8,"cssClass":"pl-c1"},{"start":9,"end":17,"cssClass":"pl-s1"},{"start":18,"end":32,"cssClass":"pl-v"},{"start":33,"end":44,"cssClass":"pl-s1"},{"start":44,"end":45,"cssClass":"pl-c1"},{"start":45,"end":453,"cssClass":"pl-s"}],[{"start":0,"end":6,"cssClass":"pl-s1"},{"start":7,"end":19,"cssClass":"pl-en"},{"start":20,"end":27,"cssClass":"pl-s"},{"start":29,"end":33,"cssClass":"pl-s1"},{"start":33,"end":34,"cssClass":"pl-c1"},{"start":34,"end":97,"cssClass":"pl-s"}],[{"start":0,"end":6,"cssClass":"pl-s1"},{"start":7,"end":19,"cssClass":"pl-en"},{"start":20,"end":27,"cssClass":"pl-s"},{"start":29,"end":33,"cssClass":"pl-s1"},{"start":33,"end":34,"cssClass":"pl-c1"},{"start":34,"end":97,"cssClass":"pl-s"}],[{"start":0,"end":4,"cssClass":"pl-s1"},{"start":5,"end":6,"cssClass":"pl-c1"},{"start":7,"end":13,"cssClass":"pl-s1"},{"start":14,"end":24,"cssClass":"pl-en"}],[],[{"start":0,"end":2,"cssClass":"pl-s1"},{"start":3,"end":4,"cssClass":"pl-c1"},{"start":5,"end":9,"cssClass":"pl-s1"},{"start":10,"end":15,"cssClass":"pl-s1"},{"start":16,"end":22,"cssClass":"pl-en"},{"start":23,"end":28,"cssClass":"pl-s"}],[{"start":0,"end":2,"cssClass":"pl-s1"},{"start":3,"end":4,"cssClass":"pl-c1"},{"start":5,"end":9,"cssClass":"pl-s1"},{"start":10,"end":15,"cssClass":"pl-s1"},{"start":16,"end":22,"cssClass":"pl-en"},{"start":23,"end":28,"cssClass":"pl-s"}],[],[{"start":0,"end":2,"cssClass":"pl-s1"},{"start":3,"end":4,"cssClass":"pl-c1"},{"start":5,"end":9,"cssClass":"pl-en"},{"start":10,"end":12,"cssClass":"pl-s1"},{"start":14,"end":16,"cssClass":"pl-s1"}],[],[{"start":0,"end":5,"cssClass":"pl-k"},{"start":6,"end":8,"cssClass":"pl-s1"},{"start":9,"end":15,"cssClass":"pl-en"},{"start":16,"end":21,"cssClass":"pl-s"}],[]],"csv":null,"csvError":null,"dependabotInfo":{"showConfigurationBanner":false,"configFilePath":null,"networkDependabotPath":"/SpiderLabs/cribdrag/network/updates","dismissConfigurationNoticePath":"/settings/dismiss-notice/dependabot_configuration_notice","configurationNoticeDismissed":null,"repoAlertsPath":"/SpiderLabs/cribdrag/security/dependabot","repoSecurityAndAnalysisPath":"/SpiderLabs/cribdrag/settings/security_analysis","repoOwnerIsOrg":true,"currentUserCanAdminRepo":false},"displayName":"xorstrings.py","displayUrl":"https://github.com/SpiderLabs/cribdrag/blob/master/xorstrings.py?raw=true","headerInfo":{"blobSize":"1.92 KB","deleteInfo":{"deleteTooltip":"You must be signed in to make or propose changes"},"editInfo":{"editTooltip":"You must be signed in to make or propose changes"},"ghDesktopPath":"https://desktop.github.com","gitLfsPath":null,"onBranch":true,"shortPath":"13988d3","siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2FSpiderLabs%2Fcribdrag%2Fblob%2Fmaster%2Fxorstrings.py","isCSV":false,"isRichtext":false,"toc":null,"lineInfo":{"truncatedLoc":"34","truncatedSloc":"26"},"mode":"executable file"},"image":false,"isCodeownersFile":null,"isPlain":false,"isValidLegacyIssueTemplate":false,"issueTemplateHelpUrl":"https://docs.github.com/articles/about-issue-and-pull-request-templates","issueTemplate":null,"discussionTemplate":null,"language":"Python","languageID":303,"large":false,"loggedIn":false,"newDiscussionPath":"/SpiderLabs/cribdrag/discussions/new","newIssuePath":"/SpiderLabs/cribdrag/issues/new","planSupportInfo":{"repoIsFork":null,"repoOwnedByCurrentUser":null,"requestFullPath":"/SpiderLabs/cribdrag/blob/master/xorstrings.py","showFreeOrgGatedFeatureMessage":null,"showPlanSupportBanner":null,"upgradeDataAttributes":null,"upgradePath":null},"publishBannersInfo":{"dismissActionNoticePath":"/settings/dismiss-notice/publish_action_from_dockerfile","releasePath":"/SpiderLabs/cribdrag/releases/new?marketplace=true","showPublishActionBanner":false},"rawBlobUrl":"https://github.com/SpiderLabs/cribdrag/raw/master/xorstrings.py","renderImageOrRaw":false,"richText":null,"renderedFileInfo":null,"shortPath":null,"symbolsEnabled":true,"tabSize":8,"topBannersInfo":{"overridingGlobalFundingFile":false,"globalPreferredFundingPath":null,"repoOwner":"SpiderLabs","repoName":"cribdrag","showInvalidCitationWarning":false,"citationHelpUrl":"https://docs.github.com/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files","showDependabotConfigurationBanner":false,"actionsOnboardingTip":null},"truncated":false,"viewable":true,"workflowRedirectUrl":null,"symbols":{"timed_out":false,"not_analyzed":false,"symbols":[{"name":"sxor","kind":"function","ident_start":830,"ident_end":834,"extent_start":826,"extent_end":1184,"fully_qualified_name":"sxor","ident_utf16":{"start":{"line_number":14,"utf16_col":4},"end":{"line_number":14,"utf16_col":8}},"extent_utf16":{"start":{"line_number":14,"utf16_col":0},"end":{"line_number":20,"utf16_col":62}}},{"name":"parser","kind":"constant","ident_start":1186,"ident_end":1192,"extent_start":1186,"extent_end":1640,"fully_qualified_name":"parser","ident_utf16":{"start":{"line_number":22,"utf16_col":0},"end":{"line_number":22,"utf16_col":6}},"extent_utf16":{"start":{"line_number":22,"utf16_col":0},"end":{"line_number":22,"utf16_col":454}}},{"name":"args","kind":"constant","ident_start":1839,"ident_end":1843,"extent_start":1839,"extent_end":1865,"fully_qualified_name":"args","ident_utf16":{"start":{"line_number":25,"utf16_col":0},"end":{"line_number":25,"utf16_col":4}},"extent_utf16":{"start":{"line_number":25,"utf16_col":0},"end":{"line_number":25,"utf16_col":26}}},{"name":"s1","kind":"constant","ident_start":1867,"ident_end":1869,"extent_start":1867,"extent_end":1896,"fully_qualified_name":"s1","ident_utf16":{"start":{"line_number":27,"utf16_col":0},"end":{"line_number":27,"utf16_col":2}},"extent_utf16":{"start":{"line_number":27,"utf16_col":0},"end":{"line_number":27,"utf16_col":29}}},{"name":"s2","kind":"constant","ident_start":1897,"ident_end":1899,"extent_start":1897,"extent_end":1926,"fully_qualified_name":"s2","ident_utf16":{"start":{"line_number":28,"utf16_col":0},"end":{"line_number":28,"utf16_col":2}},"extent_utf16":{"start":{"line_number":28,"utf16_col":0},"end":{"line_number":28,"utf16_col":29}}},{"name":"s3","kind":"constant","ident_start":1928,"ident_end":1930,"extent_start":1928,"extent_end":1945,"fully_qualified_name":"s3","ident_utf16":{"start":{"line_number":30,"utf16_col":0},"end":{"line_number":30,"utf16_col":2}},"extent_utf16":{"start":{"line_number":30,"utf16_col":0},"end":{"line_number":30,"utf16_col":17}}}]}},"copilotInfo":null,"copilotAccessAllowed":false,"csrf_tokens":{"/SpiderLabs/cribdrag/branches":{"post":"uteRVuM-UqjPERSVw8fAw-9F5jHK04Q-i9fxgvUXz7DGCmMjKbJDiBt1QfsHIYtVY-CV8rZRsmcK8BCOtkL8uw"},"/repos/preferences":{"post":"T_dKN4Sb367bBsRpWfrZc45kxscsH9GIFSZ4-OE2Q-ZQ3GfaZv-v6Rz8LcbqDtb2qa7Gx1Fp657G-TjIsFdf-Q"}}},"title":"cribdrag/xorstrings.py at master · SpiderLabs/cribdrag"}