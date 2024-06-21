#!/usr/bin/env python3
""" oab - Outlook Offline Address Books decoder
License: 3-clause BSD (see https://opensource.org/licenses/BSD-3-Clause)
Author: Hubert Tournier
"""

property_tags = {
    # mandatory rgHdrAtts:
    0x6800001F: "PidTagOfflineAddressBookName",
    0x6804001E: "PidTagOfflineAddressBookDistinguishedName",
    0x68010003: "PidTagOfflineAddressBookSequence",
    0x6802001E: "PidTagOfflineAddressBookContainerGuid",
    # optional rgHdrAtts:
    0x8C98001E: "PidTagAddressBookHierarchicalRootDepartment",
    # mandatory rgOabAtts:
    0x3003001E: "PidTagEmailAddress",
    0x39fe001F: "PidTagSmtpAddress",
    # optional rgOabAtts:
    0x3001001F: "PidTagDisplayName",
    0x8C92001F: "PidTagAddressBookPhoneticDisplayName",
    0x3A00001F: "PidTagAccount",
    0x3A11001F: "PidTagSurname",
    0x8C8F001F: "PidTagAddressBookPhoneticSurname",
    0x3A06001F: "PidTagGivenName",
    0x8C8E001F: "PidTagAddressBookPhoneticGivenName",
    0x800f101F: "PidTagAddressBookProxyAddresses",
    0x3A19001F: "PidTagOfficeLocation",
    0x39000003: "PidTagDisplayType",
    0x0FFE0003: "PidTagObjectType",
    0x3A40000B: "PidTagSendRichInfo",
    0x3A08001F: "PidTagBusinessTelephoneNumber",
    0x3A0A001F: "PidTagInitials",
    0x3A29001F: "PidTagStreetAddress",
    0x3A27001F: "PidTagLocality",
    0x3A28001F: "PidTagStateOrProvince",
    0x3A2A001F: "PidTagPostalCode",
    0x3A26001F: "PidTagCountry",
    0x3A17001F: "PidTagTitle",
    0x3A16001F: "PidTagCompanyName",
    0x8C91001F: "PidTagAddressBookPhoneticCompanyName",
    0x3A30001F: "PidTagAssistant",
    0x3A18001F: "PidTagDepartmentName",
    0x8C90001F: "PidTagAddressBookPhoneticDepartmentName",
    0x8011001F: "PidTagAddressBookTargetAddress",
    0x3A09001F: "PidTagHomeTelephoneNumber",
    0x3A1B101F: "PidTagBusiness2TelephoneNumbers",
    0x3A2F101F: "PidTagHome2TelephoneNumbers",
    0x3A23001F: "PidTagPrimaryFaxNumber",
    0x3A1C001F: "PidTagMobileTelephoneNumber",
    0x3A2E001F: "PidTagAssistantTelephoneNumber",
    0x3A21001F: "PidTagPagerTelephoneNumber",
    0x3004001F: "PidTagComment",
    0x3A220102: "PidTagUserCertificate",
    0x3A701102: "PidTagUserX509Certificate",
    0x8C6A1102: "PidTagAddressBookX509Certificate",
    0x8006001E: "PidTagAddressBookHomeMessageDatabase",
    0x39FF001E: "PidTagAddressBookDisplayNamePrintable",
    0x39050003: "PidTagDisplayTypeEx",
    0x8CA00003: "PidTagAddressBookSeniorityIndex",
    0x8CDD000B: "PidTagAddressBookHierarchicalIsHierarchicalGroup",
    0x8C6D0102: "PidTagAddressBookObjectGuid",
    0x8CAC101F: "PidTagAddressBookSenderHintTranslations",
    0x806A0003: "PidTagAddressBookDeliveryContentLength",
    0x8CB5000B: "PidTagAddressBookModerationEnabled",
    0x8CE20003: "PidTagAddressBookDistributionListMemberCount",
    0x8CE30003: "PidTagAddressBookDistributionListExternalMemberCount",
    0x8009101E: "PidTagAddressBookMember",
    0x8008101E: "PidTagAddressBookIsMemberOfDistributionList",
    0x68051003: "PidTagOfflineAddressBookTruncatedProperties",
    # truncated rgOabAtts
    0x8C9E0102: "PidTagThumbnailPhoto",
    0x8CC20102: "PidTagSpokenName",
    0x8CD8000D: "PidTagAddressBookAuthorizedSenders",
    0x8CD9000D: "PidTagAddressBookUnauthorizedSenders",
    0x8073000D: "PidTagAddressBookDistributionListMemberSubmitAccepted",
    0x8CDA000D: "PidTagAddressBookDistributionListMemberSubmitRejected",
    0x8CDB000D: "PidTagAddressBookDistributionListRejectMessagesFromDLMembers",
}
