data = [
    {
        "highestSeverity": "SUCCESS",
        "notifications": [
            {
                "severity": "SUCCESS",
                "source": "trck",
                "code": "0",
                "message": "Request was successfully processed.",
                "localizedMessage": "Request was successfully processed.",
                "messageParameters": []
            }
        ],
        "duplicateWaybill": False,
        "moreData": False,
        "trackDetailsCount": 0,
        "trackDetails": [
            {
                "notification": {
                    "severity": "SUCCESS",
                    "source": "trck",
                    "code": "0",
                    "message": "Request was successfully processed.",
                    "localizedMessage": "Request was successfully processed.",
                    "messageParameters": []
                },
                "trackingNumber": "391128701026",
                "trackingNumberUniqueIdentifier": "2458925000~391128701026~FX",
                "statusDetail": {
                    "creationTime": {
                        "$numberLong": "1584662400000"
                    },
                    "code": "DL",
                    "description": "Delivered",
                    "location": {
                        "streetLines": [],
                        "city": "Gurgaon",
                        "stateOrProvinceCode": "HR",
                        "countryCode": "IN",
                        "countryName": "India",
                        "residential": False
                    },
                    "ancillaryDetails": [
                        {
                            "reason": "11",
                            "reasonDescription": "C.O.D. payment received"
                        }
                    ]
                },
                "informationNotes": [],
                "customerExceptionRequests": [],
                "carrierCode": "FDXE",
                "operatingCompanyOrCarrierDescription": "FedEx Express",
                "otherIdentifiers": [],
                "service": {
                    "type": "FEDEX_EXPRESS_SAVER",
                    "description": "FedEx Economy",
                    "shortDescription": "XS"
                },
                "packageWeight": {
                    "units": "KG",
                    "value": 14
                },
                "shipmentWeight": {
                    "units": "KG",
                    "value": 14
                },
                "packaging": {
                    "type": "YOUR_PACKAGING",
                    "description": "Your Packaging"
                },
                "packageSequenceNumber": 1,
                "packageCount": 1,
                "shipmentContentPieceCount": 0,
                "packageContentPieceCount": 0,
                "creatorSoftwareId": "WSXI",
                "charges": [],
                "attributes": [],
                "shipmentContents": [],
                "packageContents": [],
                "commodities": [],
                "customsOptionDetails": [],
                "specialHandlings": [
                    {
                        "type": "DELIVER_WEEKDAY",
                        "description": "Deliver Weekday",
                        "paymentType": "OTHER"
                    },
                    {
                        "type": "COD",
                        "description": "Collect On Delivery (COD)",
                        "paymentType": "OTHER"
                    },
                    {
                        "type": "RESIDENTIAL_DELIVERY",
                        "description": "Residential Delivery",
                        "paymentType": "OTHER"
                    }
                ],
                "payments": [
                    {
                        "classification": "TRANSPORTATION",
                        "type": "SHIPPER_ACCOUNT",
                        "description": "Shipper"
                    },
                    {
                        "classification": "DUTIES_AND_TAXES",
                        "type": "SHIPPER_ACCOUNT",
                        "description": "Shipper"
                    }
                ],
                "shipperAddress": {
                    "streetLines": [],
                    "city": "Bangalore",
                    "stateOrProvinceCode": "KA",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "datesOrTimes": [
                    {
                        "type": "ACTUAL_DELIVERY",
                        "dateOrTimestamp": "2020-03-20T13:37:00+05:30"
                    },
                    {
                        "type": "ACTUAL_PICKUP",
                        "dateOrTimestamp": "2020-03-16T15:44:00+05:30"
                    },
                    {
                        "type": "SHIP",
                        "dateOrTimestamp": "2020-03-16T00:00:00"
                    },
                    {
                        "type": "ACTUAL_TENDER",
                        "dateOrTimestamp": "2020-03-16T15:44:00+05:30"
                    }
                ],
                "specialInstructions": [],
                "lastUpdatedDestinationAddress": {
                    "streetLines": [],
                    "city": "GURGAON",
                    "stateOrProvinceCode": "HR",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "destinationAddress": {
                    "streetLines": [],
                    "city": "Gurgaon",
                    "stateOrProvinceCode": "HR",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "actualDeliveryAddress": {
                    "streetLines": [],
                    "city": "Gurgaon",
                    "stateOrProvinceCode": "HR",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "deliveryLocationType": "RESIDENCE",
                "deliveryLocationDescription": "Residence",
                "deliveryAttempts": 0,
                "deliverySignatureName": "S.RAI",
                "pieceCountVerificationDetails": [],
                "totalUniqueAddressCountInConsolidation": 0,
                "availableImages": [
                    {
                        "type": "SIGNATURE_PROOF_OF_DELIVERY"
                    }
                ],
                "notificationEventsAvailable": [
                    "ON_DELIVERY"
                ],
                "splitShipmentParts": [],
                "deliveryOptionEligibilityDetails": [
                    {
                        "option": "INDIRECT_SIGNATURE_RELEASE",
                        "eligibility": "INELIGIBLE"
                    },
                    {
                        "option": "REDIRECT_TO_HOLD_AT_LOCATION",
                        "eligibility": "INELIGIBLE"
                    },
                    {
                        "option": "REROUTE",
                        "eligibility": "INELIGIBLE"
                    },
                    {
                        "option": "RESCHEDULE",
                        "eligibility": "INELIGIBLE"
                    }
                ],
                "events": [
                    {
                        "timestamp": {
                            "$numberLong": "1584691620000"
                        },
                        "eventType": "DL",
                        "eventDescription": "Delivered",
                        "statusExceptionCode": "11",
                        "statusExceptionDescription": "C.O.D. payment received",
                        "address": {
                            "streetLines": [],
                            "city": "Gurgaon",
                            "stateOrProvinceCode": "HR",
                            "postalCode": "122001",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "DELIVERY_LOCATION"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1584679560000"
                        },
                        "eventType": "OD",
                        "eventDescription": "On FedEx vehicle for delivery",
                        "address": {
                            "streetLines": [],
                            "city": "MANESAR",
                            "stateOrProvinceCode": "HR",
                            "postalCode": "122050",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "VEHICLE"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1584676080000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "GURGAON",
                            "stateOrProvinceCode": "HR",
                            "postalCode": "122001",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1584674160000"
                        },
                        "eventType": "AR",
                        "eventDescription": "At local FedEx facility",
                        "address": {
                            "streetLines": [],
                            "city": "MANESAR",
                            "stateOrProvinceCode": "HR",
                            "postalCode": "122050",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "DESTINATION_FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1584646440000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "GURGAON",
                            "stateOrProvinceCode": "HR",
                            "postalCode": "122001",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1584639900000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "GURGAON",
                            "stateOrProvinceCode": "HR",
                            "postalCode": "122001",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1584399780000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "562123",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1584383760000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "562123",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1584379440000"
                        },
                        "eventType": "DP",
                        "eventDescription": "Left FedEx origin facility",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "560048",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "ORIGIN_FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1584353640000"
                        },
                        "eventType": "PU",
                        "eventDescription": "Picked up",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "560048",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "PICKUP_LOCATION"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1584348235000"
                        },
                        "eventType": "OC",
                        "eventDescription": "Shipment information sent to FedEx",
                        "address": {
                            "streetLines": [],
                            "residential": False
                        },
                        "arrivalLocation": "CUSTOMER"
                    }
                ]
            }
        ]
    },
    {
        "highestSeverity": "SUCCESS",
        "notifications": [
            {
                "severity": "SUCCESS",
                "source": "trck",
                "code": "0",
                "message": "Request was successfully processed.",
                "localizedMessage": "Request was successfully processed.",
                "messageParameters": []
            }
        ],
        "duplicateWaybill": False,
        "moreData": False,
        "trackDetailsCount": 0,
        "trackDetails": [
            {
                "notification": {
                    "severity": "SUCCESS",
                    "source": "trck",
                    "code": "0",
                    "message": "Request was successfully processed.",
                    "localizedMessage": "Request was successfully processed.",
                    "messageParameters": []
                },
                "trackingNumber": "390901883808",
                "trackingNumberUniqueIdentifier": "2458915000~390901883808~FX",
                "statusDetail": {
                    "creationTime": {
                        "$numberLong": "1583712000000"
                    },
                    "code": "DL",
                    "description": "Delivered",
                    "location": {
                        "streetLines": [],
                        "city": "Bangalore",
                        "stateOrProvinceCode": "KA",
                        "countryCode": "IN",
                        "countryName": "India",
                        "residential": False
                    },
                    "ancillaryDetails": []
                },
                "informationNotes": [],
                "customerExceptionRequests": [],
                "carrierCode": "FDXE",
                "operatingCompanyOrCarrierDescription": "FedEx Express",
                "otherIdentifiers": [],
                "service": {
                    "type": "FEDEX_EXPRESS_SAVER",
                    "description": "FedEx Economy",
                    "shortDescription": "XS"
                },
                "packageWeight": {
                    "units": "KG",
                    "value": 14
                },
                "shipmentWeight": {
                    "units": "KG",
                    "value": 14
                },
                "packaging": {
                    "type": "YOUR_PACKAGING",
                    "description": "Your Packaging"
                },
                "packageSequenceNumber": 1,
                "packageCount": 1,
                "shipmentContentPieceCount": 0,
                "packageContentPieceCount": 0,
                "creatorSoftwareId": "WSXI",
                "charges": [],
                "attributes": [],
                "shipmentContents": [],
                "packageContents": [],
                "commodities": [],
                "customsOptionDetails": [],
                "specialHandlings": [
                    {
                        "type": "DELIVER_WEEKDAY",
                        "description": "Deliver Weekday",
                        "paymentType": "OTHER"
                    }
                ],
                "payments": [
                    {
                        "classification": "TRANSPORTATION",
                        "type": "SHIPPER_ACCOUNT",
                        "description": "Shipper"
                    },
                    {
                        "classification": "DUTIES_AND_TAXES",
                        "type": "SHIPPER_ACCOUNT",
                        "description": "Shipper"
                    }
                ],
                "shipperAddress": {
                    "streetLines": [],
                    "city": "Bangalore",
                    "stateOrProvinceCode": "KA",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "datesOrTimes": [
                    {
                        "type": "ACTUAL_DELIVERY",
                        "dateOrTimestamp": "2020-03-09T19:50:00+05:30"
                    },
                    {
                        "type": "ACTUAL_PICKUP",
                        "dateOrTimestamp": "2020-03-06T16:07:00+05:30"
                    },
                    {
                        "type": "SHIP",
                        "dateOrTimestamp": "2020-03-06T00:00:00"
                    },
                    {
                        "type": "ACTUAL_TENDER",
                        "dateOrTimestamp": "2020-03-06T16:07:00+05:30"
                    }
                ],
                "specialInstructions": [],
                "lastUpdatedDestinationAddress": {
                    "streetLines": [],
                    "city": "BANGALORE",
                    "stateOrProvinceCode": "KA",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "destinationAddress": {
                    "streetLines": [],
                    "city": "Bangalore",
                    "stateOrProvinceCode": "KA",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "actualDeliveryAddress": {
                    "streetLines": [],
                    "city": "Bangalore",
                    "stateOrProvinceCode": "KA",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "deliveryLocationType": "RECEPTIONIST_OR_FRONT_DESK",
                "deliveryLocationDescription": "Receptionist/Front Desk",
                "deliveryAttempts": 0,
                "deliverySignatureName": "S.IGN",
                "pieceCountVerificationDetails": [],
                "totalUniqueAddressCountInConsolidation": 0,
                "availableImages": [],
                "notificationEventsAvailable": [
                    "ON_DELIVERY"
                ],
                "splitShipmentParts": [],
                "deliveryOptionEligibilityDetails": [
                    {
                        "option": "INDIRECT_SIGNATURE_RELEASE",
                        "eligibility": "INELIGIBLE"
                    },
                    {
                        "option": "REDIRECT_TO_HOLD_AT_LOCATION",
                        "eligibility": "INELIGIBLE"
                    },
                    {
                        "option": "REROUTE",
                        "eligibility": "INELIGIBLE"
                    },
                    {
                        "option": "RESCHEDULE",
                        "eligibility": "INELIGIBLE"
                    }
                ],
                "events": [
                    {
                        "timestamp": {
                            "$numberLong": "1583763600000"
                        },
                        "eventType": "DL",
                        "eventDescription": "Delivered",
                        "address": {
                            "streetLines": [],
                            "city": "Bangalore",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "560034",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "DELIVERY_LOCATION"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583731200000"
                        },
                        "eventType": "OD",
                        "eventDescription": "On FedEx vehicle for delivery",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "560100",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "VEHICLE"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583731140000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "statusExceptionCode": "67",
                        "statusExceptionDescription": "Tendered to authorized agent for final delivery",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "560100",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583729700000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "statusExceptionCode": "67",
                        "statusExceptionDescription": "Tendered to authorized agent for final delivery",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "560100",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583729700000"
                        },
                        "eventType": "OD",
                        "eventDescription": "On FedEx vehicle for delivery",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "560100",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "VEHICLE"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583721480000"
                        },
                        "eventType": "AR",
                        "eventDescription": "At local FedEx facility",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "560100",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "DESTINATION_FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583624760000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "562123",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583525400000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "562123",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583525400000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "562123",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583514660000"
                        },
                        "eventType": "DP",
                        "eventDescription": "Left FedEx origin facility",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "560048",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "ORIGIN_FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583491020000"
                        },
                        "eventType": "PU",
                        "eventDescription": "Picked up",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "560048",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "PICKUP_LOCATION"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583476076000"
                        },
                        "eventType": "OC",
                        "eventDescription": "Shipment information sent to FedEx",
                        "address": {
                            "streetLines": [],
                            "residential": False
                        },
                        "arrivalLocation": "CUSTOMER"
                    }
                ]
            }
        ]
    },
    {
        "highestSeverity": "SUCCESS",
        "notifications": [
            {
                "severity": "SUCCESS",
                "source": "trck",
                "code": "0",
                "message": "Request was successfully processed.",
                "localizedMessage": "Request was successfully processed.",
                "messageParameters": []
            }
        ],
        "duplicateWaybill": False,
        "moreData": False,
        "trackDetailsCount": 0,
        "trackDetails": [
            {
                "notification": {
                    "severity": "SUCCESS",
                    "source": "trck",
                    "code": "0",
                    "message": "Request was successfully processed.",
                    "localizedMessage": "Request was successfully processed.",
                    "messageParameters": []
                },
                "trackingNumber": "391128749178",
                "trackingNumberUniqueIdentifier": "2458925000~391128749178~FX",
                "statusDetail": {
                    "creationTime": {
                        "$numberLong": "1584576000000"
                    },
                    "code": "DL",
                    "description": "Delivered",
                    "location": {
                        "streetLines": [],
                        "city": "Ahmedabad",
                        "stateOrProvinceCode": "GJ",
                        "countryCode": "IN",
                        "countryName": "India",
                        "residential": False
                    },
                    "ancillaryDetails": []
                },
                "informationNotes": [],
                "customerExceptionRequests": [],
                "carrierCode": "FDXE",
                "operatingCompanyOrCarrierDescription": "FedEx Express",
                "otherIdentifiers": [],
                "service": {
                    "type": "FEDEX_EXPRESS_SAVER",
                    "description": "FedEx Economy",
                    "shortDescription": "XS"
                },
                "packageWeight": {
                    "units": "KG",
                    "value": 14
                },
                "shipmentWeight": {
                    "units": "KG",
                    "value": 14
                },
                "packaging": {
                    "type": "YOUR_PACKAGING",
                    "description": "Your Packaging"
                },
                "packageSequenceNumber": 1,
                "packageCount": 1,
                "shipmentContentPieceCount": 0,
                "packageContentPieceCount": 0,
                "creatorSoftwareId": "WSXI",
                "charges": [],
                "attributes": [],
                "shipmentContents": [],
                "packageContents": [],
                "commodities": [],
                "customsOptionDetails": [],
                "specialHandlings": [
                    {
                        "type": "DELIVER_WEEKDAY",
                        "description": "Deliver Weekday",
                        "paymentType": "OTHER"
                    },
                    {
                        "type": "RESIDENTIAL_DELIVERY",
                        "description": "Residential Delivery",
                        "paymentType": "OTHER"
                    }
                ],
                "payments": [
                    {
                        "classification": "TRANSPORTATION",
                        "type": "SHIPPER_ACCOUNT",
                        "description": "Shipper"
                    },
                    {
                        "classification": "DUTIES_AND_TAXES",
                        "type": "SHIPPER_ACCOUNT",
                        "description": "Shipper"
                    }
                ],
                "shipperAddress": {
                    "streetLines": [],
                    "city": "Bangalore",
                    "stateOrProvinceCode": "KA",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "datesOrTimes": [
                    {
                        "type": "ACTUAL_DELIVERY",
                        "dateOrTimestamp": "2020-03-19T15:29:00+05:30"
                    },
                    {
                        "type": "ACTUAL_PICKUP",
                        "dateOrTimestamp": "2020-03-16T15:44:00+05:30"
                    },
                    {
                        "type": "SHIP",
                        "dateOrTimestamp": "2020-03-16T00:00:00"
                    },
                    {
                        "type": "ACTUAL_TENDER",
                        "dateOrTimestamp": "2020-03-16T15:44:00+05:30"
                    }
                ],
                "specialInstructions": [],
                "lastUpdatedDestinationAddress": {
                    "streetLines": [],
                    "city": "AHMEDABAD",
                    "stateOrProvinceCode": "GJ",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "destinationAddress": {
                    "streetLines": [],
                    "city": "Ahmedabad",
                    "stateOrProvinceCode": "GJ",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "actualDeliveryAddress": {
                    "streetLines": [],
                    "city": "Ahmedabad",
                    "stateOrProvinceCode": "GJ",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "deliveryLocationType": "RESIDENCE",
                "deliveryLocationDescription": "Residence",
                "deliveryAttempts": 0,
                "deliverySignatureName": "I.IMRANBHAI",
                "pieceCountVerificationDetails": [],
                "totalUniqueAddressCountInConsolidation": 0,
                "availableImages": [
                    {
                        "type": "SIGNATURE_PROOF_OF_DELIVERY"
                    }
                ],
                "notificationEventsAvailable": [
                    "ON_DELIVERY"
                ],
                "splitShipmentParts": [],
                "deliveryOptionEligibilityDetails": [
                    {
                        "option": "INDIRECT_SIGNATURE_RELEASE",
                        "eligibility": "INELIGIBLE"
                    },
                    {
                        "option": "REDIRECT_TO_HOLD_AT_LOCATION",
                        "eligibility": "INELIGIBLE"
                    },
                    {
                        "option": "REROUTE",
                        "eligibility": "INELIGIBLE"
                    },
                    {
                        "option": "RESCHEDULE",
                        "eligibility": "INELIGIBLE"
                    }
                ],
                "events": [
                    {
                        "timestamp": {
                            "$numberLong": "1584611940000"
                        },
                        "eventType": "DL",
                        "eventDescription": "Delivered",
                        "address": {
                            "streetLines": [],
                            "city": "Ahmedabad",
                            "stateOrProvinceCode": "GJ",
                            "postalCode": "380028",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "DELIVERY_LOCATION"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1584601200000"
                        },
                        "eventType": "OD",
                        "eventDescription": "On FedEx vehicle for delivery",
                        "address": {
                            "streetLines": [],
                            "city": "AHMEDABAD",
                            "stateOrProvinceCode": "GJ",
                            "postalCode": "380009",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "VEHICLE"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1584582600000"
                        },
                        "eventType": "AR",
                        "eventDescription": "At local FedEx facility",
                        "address": {
                            "streetLines": [],
                            "city": "AHMEDABAD",
                            "stateOrProvinceCode": "GJ",
                            "postalCode": "380009",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "DESTINATION_FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1584571140000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "AHMEDABAD",
                            "stateOrProvinceCode": "GJ",
                            "postalCode": "382213",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1584571080000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "AHMEDABAD",
                            "stateOrProvinceCode": "GJ",
                            "postalCode": "382213",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1584489300000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "NAVI MUMBAI",
                            "stateOrProvinceCode": "MH",
                            "postalCode": "410218",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1584479580000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "NAVI MUMBAI",
                            "stateOrProvinceCode": "MH",
                            "postalCode": "410218",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1584392520000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "562123",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1584383760000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "562123",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1584379440000"
                        },
                        "eventType": "DP",
                        "eventDescription": "Left FedEx origin facility",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "560048",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "ORIGIN_FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1584353640000"
                        },
                        "eventType": "PU",
                        "eventDescription": "Picked up",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "560048",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "PICKUP_LOCATION"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1584348544000"
                        },
                        "eventType": "OC",
                        "eventDescription": "Shipment information sent to FedEx",
                        "address": {
                            "streetLines": [],
                            "residential": False
                        },
                        "arrivalLocation": "CUSTOMER"
                    }
                ]
            }
        ]
    },
    {
        "highestSeverity": "SUCCESS",
        "notifications": [
            {
                "severity": "SUCCESS",
                "source": "trck",
                "code": "0",
                "message": "Request was successfully processed.",
                "localizedMessage": "Request was successfully processed.",
                "messageParameters": []
            }
        ],
        "duplicateWaybill": False,
        "moreData": False,
        "trackDetailsCount": 0,
        "trackDetails": [
            {
                "notification": {
                    "severity": "SUCCESS",
                    "source": "trck",
                    "code": "0",
                    "message": "Request was successfully processed.",
                    "localizedMessage": "Request was successfully processed.",
                    "messageParameters": []
                },
                "trackingNumber": "390807986805",
                "trackingNumberUniqueIdentifier": "2458912000~390807986805~FX",
                "statusDetail": {
                    "creationTime": {
                        "$numberLong": "1583539200000"
                    },
                    "code": "DL",
                    "description": "Delivered",
                    "location": {
                        "streetLines": [],
                        "city": "New Delhi",
                        "stateOrProvinceCode": "DL",
                        "countryCode": "IN",
                        "countryName": "India",
                        "residential": False
                    },
                    "ancillaryDetails": []
                },
                "informationNotes": [],
                "customerExceptionRequests": [],
                "carrierCode": "FDXE",
                "operatingCompanyOrCarrierDescription": "FedEx Express",
                "otherIdentifiers": [],
                "service": {
                    "type": "FEDEX_EXPRESS_SAVER",
                    "description": "FedEx Economy",
                    "shortDescription": "XS"
                },
                "packageWeight": {
                    "units": "KG",
                    "value": 14
                },
                "shipmentWeight": {
                    "units": "KG",
                    "value": 14
                },
                "packaging": {
                    "type": "YOUR_PACKAGING",
                    "description": "Your Packaging"
                },
                "packageSequenceNumber": 1,
                "packageCount": 1,
                "shipmentContentPieceCount": 0,
                "packageContentPieceCount": 0,
                "creatorSoftwareId": "WSXI",
                "charges": [],
                "attributes": [],
                "shipmentContents": [],
                "packageContents": [],
                "commodities": [],
                "customsOptionDetails": [],
                "specialHandlings": [
                    {
                        "type": "DELIVER_WEEKDAY",
                        "description": "Deliver Weekday",
                        "paymentType": "OTHER"
                    },
                    {
                        "type": "RESIDENTIAL_DELIVERY",
                        "description": "Residential Delivery",
                        "paymentType": "OTHER"
                    }
                ],
                "payments": [
                    {
                        "classification": "TRANSPORTATION",
                        "type": "SHIPPER_ACCOUNT",
                        "description": "Shipper"
                    },
                    {
                        "classification": "DUTIES_AND_TAXES",
                        "type": "SHIPPER_ACCOUNT",
                        "description": "Shipper"
                    }
                ],
                "shipperAddress": {
                    "streetLines": [],
                    "city": "Bangalore",
                    "stateOrProvinceCode": "KA",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "datesOrTimes": [
                    {
                        "type": "ACTUAL_DELIVERY",
                        "dateOrTimestamp": "2020-03-07T14:24:00+05:30"
                    },
                    {
                        "type": "ACTUAL_PICKUP",
                        "dateOrTimestamp": "2020-03-03T16:19:00+05:30"
                    },
                    {
                        "type": "SHIP",
                        "dateOrTimestamp": "2020-03-03T00:00:00"
                    },
                    {
                        "type": "ACTUAL_TENDER",
                        "dateOrTimestamp": "2020-03-03T16:19:00+05:30"
                    }
                ],
                "specialInstructions": [],
                "lastUpdatedDestinationAddress": {
                    "streetLines": [],
                    "city": "NEW DELHI",
                    "stateOrProvinceCode": "DL",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "destinationAddress": {
                    "streetLines": [],
                    "city": "New Delhi",
                    "stateOrProvinceCode": "DL",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "actualDeliveryAddress": {
                    "streetLines": [],
                    "city": "New Delhi",
                    "stateOrProvinceCode": "DL",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "deliveryLocationType": "RESIDENCE",
                "deliveryLocationDescription": "Residence",
                "deliveryAttempts": 0,
                "deliverySignatureName": "G.GUNJAN",
                "pieceCountVerificationDetails": [],
                "totalUniqueAddressCountInConsolidation": 0,
                "availableImages": [
                    {
                        "type": "SIGNATURE_PROOF_OF_DELIVERY"
                    }
                ],
                "notificationEventsAvailable": [
                    "ON_DELIVERY"
                ],
                "splitShipmentParts": [],
                "deliveryOptionEligibilityDetails": [
                    {
                        "option": "INDIRECT_SIGNATURE_RELEASE",
                        "eligibility": "INELIGIBLE"
                    },
                    {
                        "option": "REDIRECT_TO_HOLD_AT_LOCATION",
                        "eligibility": "INELIGIBLE"
                    },
                    {
                        "option": "REROUTE",
                        "eligibility": "INELIGIBLE"
                    },
                    {
                        "option": "RESCHEDULE",
                        "eligibility": "INELIGIBLE"
                    }
                ],
                "events": [
                    {
                        "timestamp": {
                            "$numberLong": "1583571240000"
                        },
                        "eventType": "DL",
                        "eventDescription": "Delivered",
                        "address": {
                            "streetLines": [],
                            "city": "New Delhi",
                            "stateOrProvinceCode": "DL",
                            "postalCode": "110088",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "DELIVERY_LOCATION"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583557020000"
                        },
                        "eventType": "OD",
                        "eventDescription": "On FedEx vehicle for delivery",
                        "address": {
                            "streetLines": [],
                            "city": "NEW DELHI",
                            "stateOrProvinceCode": "DL",
                            "postalCode": "110042",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "VEHICLE"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583553600000"
                        },
                        "eventType": "AR",
                        "eventDescription": "At local FedEx facility",
                        "address": {
                            "streetLines": [],
                            "city": "NEW DELHI",
                            "stateOrProvinceCode": "DL",
                            "postalCode": "110042",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "DESTINATION_FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583535480000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "GURGAON",
                            "stateOrProvinceCode": "HR",
                            "postalCode": "122001",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583522640000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "GURGAON",
                            "stateOrProvinceCode": "HR",
                            "postalCode": "122001",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583521980000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "GURGAON",
                            "stateOrProvinceCode": "HR",
                            "postalCode": "122001",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583277180000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "562123",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583259780000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "562123",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583232540000"
                        },
                        "eventType": "PU",
                        "eventDescription": "Picked up",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "560048",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "PICKUP_LOCATION"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583219078000"
                        },
                        "eventType": "OC",
                        "eventDescription": "Shipment information sent to FedEx",
                        "address": {
                            "streetLines": [],
                            "residential": False
                        },
                        "arrivalLocation": "CUSTOMER"
                    }
                ]
            }
        ]
    },
    {
        "highestSeverity": "SUCCESS",
        "notifications": [
            {
                "severity": "SUCCESS",
                "source": "trck",
                "code": "0",
                "message": "Request was successfully processed.",
                "localizedMessage": "Request was successfully processed.",
                "messageParameters": []
            }
        ],
        "duplicateWaybill": False,
        "moreData": False,
        "trackDetailsCount": 0,
        "trackDetails": [
            {
                "notification": {
                    "severity": "SUCCESS",
                    "source": "trck",
                    "code": "0",
                    "message": "Request was successfully processed.",
                    "localizedMessage": "Request was successfully processed.",
                    "messageParameters": []
                },
                "trackingNumber": "390948921190",
                "trackingNumberUniqueIdentifier": "2458918000~390948921190~FX",
                "statusDetail": {
                    "creationTime": {
                        "$numberLong": "1584057600000"
                    },
                    "code": "DL",
                    "description": "Delivered",
                    "location": {
                        "streetLines": [],
                        "city": "Delhi",
                        "stateOrProvinceCode": "DL",
                        "countryCode": "IN",
                        "countryName": "India",
                        "residential": False
                    },
                    "ancillaryDetails": []
                },
                "informationNotes": [],
                "customerExceptionRequests": [],
                "carrierCode": "FDXE",
                "operatingCompanyOrCarrierDescription": "FedEx Express",
                "otherIdentifiers": [],
                "service": {
                    "type": "FEDEX_EXPRESS_SAVER",
                    "description": "FedEx Economy",
                    "shortDescription": "XS"
                },
                "packageWeight": {
                    "units": "KG",
                    "value": 14
                },
                "shipmentWeight": {
                    "units": "KG",
                    "value": 14
                },
                "packaging": {
                    "type": "YOUR_PACKAGING",
                    "description": "Your Packaging"
                },
                "packageSequenceNumber": 1,
                "packageCount": 1,
                "shipmentContentPieceCount": 0,
                "packageContentPieceCount": 0,
                "creatorSoftwareId": "WSXI",
                "charges": [],
                "attributes": [],
                "shipmentContents": [],
                "packageContents": [],
                "commodities": [],
                "customsOptionDetails": [],
                "specialHandlings": [
                    {
                        "type": "DELIVER_WEEKDAY",
                        "description": "Deliver Weekday",
                        "paymentType": "OTHER"
                    },
                    {
                        "type": "COD",
                        "description": "Collect On Delivery (COD)",
                        "paymentType": "OTHER"
                    },
                    {
                        "type": "RESIDENTIAL_DELIVERY",
                        "description": "Residential Delivery",
                        "paymentType": "OTHER"
                    }
                ],
                "payments": [
                    {
                        "classification": "TRANSPORTATION",
                        "type": "SHIPPER_ACCOUNT",
                        "description": "Shipper"
                    },
                    {
                        "classification": "DUTIES_AND_TAXES",
                        "type": "SHIPPER_ACCOUNT",
                        "description": "Shipper"
                    }
                ],
                "shipperAddress": {
                    "streetLines": [],
                    "city": "Bangalore",
                    "stateOrProvinceCode": "KA",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "datesOrTimes": [
                    {
                        "type": "ACTUAL_DELIVERY",
                        "dateOrTimestamp": "2020-03-13T14:44:00+05:30"
                    },
                    {
                        "type": "ACTUAL_PICKUP",
                        "dateOrTimestamp": "2020-03-09T15:12:00+05:30"
                    },
                    {
                        "type": "SHIP",
                        "dateOrTimestamp": "2020-03-09T00:00:00"
                    },
                    {
                        "type": "ACTUAL_TENDER",
                        "dateOrTimestamp": "2020-03-09T15:12:00+05:30"
                    }
                ],
                "specialInstructions": [],
                "lastUpdatedDestinationAddress": {
                    "streetLines": [],
                    "city": "DELHI",
                    "stateOrProvinceCode": "DL",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "destinationAddress": {
                    "streetLines": [],
                    "city": "Delhi",
                    "stateOrProvinceCode": "DL",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "actualDeliveryAddress": {
                    "streetLines": [],
                    "city": "Delhi",
                    "stateOrProvinceCode": "DL",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "deliveryLocationType": "RESIDENCE",
                "deliveryLocationDescription": "Residence",
                "deliveryAttempts": 0,
                "deliverySignatureName": "M.MOHIT",
                "pieceCountVerificationDetails": [],
                "totalUniqueAddressCountInConsolidation": 0,
                "availableImages": [
                    {
                        "type": "SIGNATURE_PROOF_OF_DELIVERY"
                    }
                ],
                "notificationEventsAvailable": [
                    "ON_DELIVERY"
                ],
                "splitShipmentParts": [],
                "deliveryOptionEligibilityDetails": [
                    {
                        "option": "INDIRECT_SIGNATURE_RELEASE",
                        "eligibility": "INELIGIBLE"
                    },
                    {
                        "option": "REDIRECT_TO_HOLD_AT_LOCATION",
                        "eligibility": "INELIGIBLE"
                    },
                    {
                        "option": "REROUTE",
                        "eligibility": "INELIGIBLE"
                    },
                    {
                        "option": "RESCHEDULE",
                        "eligibility": "INELIGIBLE"
                    }
                ],
                "events": [
                    {
                        "timestamp": {
                            "$numberLong": "1584090840000"
                        },
                        "eventType": "DL",
                        "eventDescription": "Delivered",
                        "address": {
                            "streetLines": [],
                            "city": "Delhi",
                            "stateOrProvinceCode": "DL",
                            "postalCode": "110009",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "DELIVERY_LOCATION"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1584072120000"
                        },
                        "eventType": "OD",
                        "eventDescription": "On FedEx vehicle for delivery",
                        "address": {
                            "streetLines": [],
                            "city": "NEW DELHI",
                            "stateOrProvinceCode": "DL",
                            "postalCode": "110042",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "VEHICLE"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1584071820000"
                        },
                        "eventType": "AR",
                        "eventDescription": "At local FedEx facility",
                        "address": {
                            "streetLines": [],
                            "city": "NEW DELHI",
                            "stateOrProvinceCode": "DL",
                            "postalCode": "110042",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "DESTINATION_FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1584052680000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "GURGAON",
                            "stateOrProvinceCode": "HR",
                            "postalCode": "122001",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1584041160000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "GURGAON",
                            "stateOrProvinceCode": "HR",
                            "postalCode": "122001",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1584037200000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "GURGAON",
                            "stateOrProvinceCode": "HR",
                            "postalCode": "122001",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583796000000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "562123",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583781180000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "562123",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583773020000"
                        },
                        "eventType": "DP",
                        "eventDescription": "Left FedEx origin facility",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "560048",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "ORIGIN_FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583746920000"
                        },
                        "eventType": "PU",
                        "eventDescription": "Picked up",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "560048",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "PICKUP_LOCATION"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583734164000"
                        },
                        "eventType": "OC",
                        "eventDescription": "Shipment information sent to FedEx",
                        "address": {
                            "streetLines": [],
                            "residential": False
                        },
                        "arrivalLocation": "CUSTOMER"
                    }
                ]
            }
        ]
    },
    {
        "highestSeverity": "SUCCESS",
        "notifications": [
            {
                "severity": "SUCCESS",
                "source": "trck",
                "code": "0",
                "message": "Request was successfully processed.",
                "localizedMessage": "Request was successfully processed.",
                "messageParameters": []
            }
        ],
        "duplicateWaybill": False,
        "moreData": False,
        "trackDetailsCount": 0,
        "trackDetails": [
            {
                "notification": {
                    "severity": "SUCCESS",
                    "source": "trck",
                    "code": "0",
                    "message": "Request was successfully processed.",
                    "localizedMessage": "Request was successfully processed.",
                    "messageParameters": []
                },
                "trackingNumber": "390950106897",
                "trackingNumberUniqueIdentifier": "2458918000~390950106897~FX",
                "statusDetail": {
                    "creationTime": {
                        "$numberLong": "1583971200000"
                    },
                    "code": "DL",
                    "description": "Delivered",
                    "location": {
                        "streetLines": [],
                        "city": "Mumbai",
                        "stateOrProvinceCode": "MH",
                        "countryCode": "IN",
                        "countryName": "India",
                        "residential": False
                    },
                    "ancillaryDetails": []
                },
                "informationNotes": [],
                "customerExceptionRequests": [],
                "carrierCode": "FDXE",
                "operatingCompanyOrCarrierDescription": "FedEx Express",
                "otherIdentifiers": [],
                "service": {
                    "type": "FEDEX_EXPRESS_SAVER",
                    "description": "FedEx Economy",
                    "shortDescription": "XS"
                },
                "packageWeight": {
                    "units": "KG",
                    "value": 14
                },
                "packageDimensions": {
                    "length": 38,
                    "width": 25,
                    "height": 61,
                    "units": "CM"
                },
                "shipmentWeight": {
                    "units": "KG",
                    "value": 14
                },
                "packaging": {
                    "type": "YOUR_PACKAGING",
                    "description": "Your Packaging"
                },
                "packageSequenceNumber": 1,
                "packageCount": 1,
                "shipmentContentPieceCount": 0,
                "packageContentPieceCount": 0,
                "creatorSoftwareId": "WSXI",
                "charges": [],
                "attributes": [],
                "shipmentContents": [],
                "packageContents": [],
                "commodities": [],
                "customsOptionDetails": [],
                "specialHandlings": [
                    {
                        "type": "DELIVER_WEEKDAY",
                        "description": "Deliver Weekday",
                        "paymentType": "OTHER"
                    }
                ],
                "payments": [
                    {
                        "classification": "TRANSPORTATION",
                        "type": "SHIPPER_ACCOUNT",
                        "description": "Shipper"
                    },
                    {
                        "classification": "DUTIES_AND_TAXES",
                        "type": "SHIPPER_ACCOUNT",
                        "description": "Shipper"
                    }
                ],
                "shipperAddress": {
                    "streetLines": [],
                    "city": "Bangalore",
                    "stateOrProvinceCode": "KA",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "datesOrTimes": [
                    {
                        "type": "ACTUAL_DELIVERY",
                        "dateOrTimestamp": "2020-03-12T16:00:00+05:30"
                    },
                    {
                        "type": "ACTUAL_PICKUP",
                        "dateOrTimestamp": "2020-03-09T15:12:00+05:30"
                    },
                    {
                        "type": "SHIP",
                        "dateOrTimestamp": "2020-03-09T00:00:00"
                    },
                    {
                        "type": "ACTUAL_TENDER",
                        "dateOrTimestamp": "2020-03-09T15:12:00+05:30"
                    }
                ],
                "specialInstructions": [],
                "lastUpdatedDestinationAddress": {
                    "streetLines": [],
                    "city": "MUMBAI",
                    "stateOrProvinceCode": "MH",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "destinationAddress": {
                    "streetLines": [],
                    "city": "Mumbai",
                    "stateOrProvinceCode": "MH",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "actualDeliveryAddress": {
                    "streetLines": [],
                    "city": "Mumbai",
                    "stateOrProvinceCode": "MH",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "deliveryAttempts": 0,
                "deliverySignatureName": "SIGN",
                "pieceCountVerificationDetails": [],
                "totalUniqueAddressCountInConsolidation": 0,
                "availableImages": [],
                "notificationEventsAvailable": [
                    "ON_DELIVERY"
                ],
                "splitShipmentParts": [],
                "deliveryOptionEligibilityDetails": [
                    {
                        "option": "INDIRECT_SIGNATURE_RELEASE",
                        "eligibility": "INELIGIBLE"
                    },
                    {
                        "option": "REDIRECT_TO_HOLD_AT_LOCATION",
                        "eligibility": "INELIGIBLE"
                    },
                    {
                        "option": "REROUTE",
                        "eligibility": "INELIGIBLE"
                    },
                    {
                        "option": "RESCHEDULE",
                        "eligibility": "INELIGIBLE"
                    }
                ],
                "events": [
                    {
                        "timestamp": {
                            "$numberLong": "1584009000000"
                        },
                        "eventType": "DL",
                        "eventDescription": "Delivered",
                        "address": {
                            "streetLines": [],
                            "city": "Mumbai",
                            "stateOrProvinceCode": "MH",
                            "postalCode": "400053",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "DELIVERY_LOCATION"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583988660000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "statusExceptionCode": "67",
                        "statusExceptionDescription": "Tendered to authorized agent for final delivery",
                        "address": {
                            "streetLines": [],
                            "city": "MUMBAI",
                            "stateOrProvinceCode": "MH",
                            "postalCode": "400053",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583925720000"
                        },
                        "eventType": "AR",
                        "eventDescription": "At local FedEx facility",
                        "address": {
                            "streetLines": [],
                            "city": "MUMBAI",
                            "stateOrProvinceCode": "MH",
                            "postalCode": "400053",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "DESTINATION_FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583916360000"
                        },
                        "eventType": "DE",
                        "eventDescription": "Delivery exception",
                        "statusExceptionCode": "31",
                        "statusExceptionDescription": "Package at station, arrived after courier dispatch",
                        "address": {
                            "streetLines": [],
                            "city": "MUMBAI",
                            "stateOrProvinceCode": "MH",
                            "postalCode": "400053",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "DESTINATION_FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583916000000"
                        },
                        "eventType": "AR",
                        "eventDescription": "At local FedEx facility",
                        "address": {
                            "streetLines": [],
                            "city": "MUMBAI",
                            "stateOrProvinceCode": "MH",
                            "postalCode": "400053",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "DESTINATION_FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583896620000"
                        },
                        "eventType": "AR",
                        "eventDescription": "At local FedEx facility",
                        "address": {
                            "streetLines": [],
                            "city": "MUMBAI",
                            "stateOrProvinceCode": "MH",
                            "postalCode": "400059",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "DESTINATION_FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583884440000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "BHIWANDI",
                            "stateOrProvinceCode": "MH",
                            "postalCode": "421302",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583784360000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "562123",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583781180000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "562123",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583773020000"
                        },
                        "eventType": "DP",
                        "eventDescription": "Left FedEx origin facility",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "560048",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "ORIGIN_FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583746920000"
                        },
                        "eventType": "PU",
                        "eventDescription": "Picked up",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "560048",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "PICKUP_LOCATION"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583742568000"
                        },
                        "eventType": "OC",
                        "eventDescription": "Shipment information sent to FedEx",
                        "address": {
                            "streetLines": [],
                            "residential": False
                        },
                        "arrivalLocation": "CUSTOMER"
                    }
                ]
            }
        ]
    },
    {
        "highestSeverity": "SUCCESS",
        "notifications": [
            {
                "severity": "SUCCESS",
                "source": "trck",
                "code": "0",
                "message": "Request was successfully processed.",
                "localizedMessage": "Request was successfully processed.",
                "messageParameters": []
            }
        ],
        "duplicateWaybill": False,
        "moreData": False,
        "trackDetailsCount": 0,
        "trackDetails": [
            {
                "notification": {
                    "severity": "SUCCESS",
                    "source": "trck",
                    "code": "0",
                    "message": "Request was successfully processed.",
                    "localizedMessage": "Request was successfully processed.",
                    "messageParameters": []
                },
                "trackingNumber": "391128762808",
                "trackingNumberUniqueIdentifier": "2458925000~391128762808~FX",
                "statusDetail": {
                    "creationTime": {
                        "$numberLong": "1584489600000"
                    },
                    "code": "DL",
                    "description": "Delivered",
                    "location": {
                        "streetLines": [],
                        "city": "Mumbai",
                        "stateOrProvinceCode": "MH",
                        "countryCode": "IN",
                        "countryName": "India",
                        "residential": False
                    },
                    "ancillaryDetails": []
                },
                "informationNotes": [],
                "customerExceptionRequests": [],
                "carrierCode": "FDXE",
                "operatingCompanyOrCarrierDescription": "FedEx Express",
                "otherIdentifiers": [],
                "service": {
                    "type": "FEDEX_EXPRESS_SAVER",
                    "description": "FedEx Economy",
                    "shortDescription": "XS"
                },
                "packageWeight": {
                    "units": "KG",
                    "value": 14
                },
                "shipmentWeight": {
                    "units": "KG",
                    "value": 14
                },
                "packaging": {
                    "type": "YOUR_PACKAGING",
                    "description": "Your Packaging"
                },
                "packageSequenceNumber": 1,
                "packageCount": 1,
                "shipmentContentPieceCount": 0,
                "packageContentPieceCount": 0,
                "creatorSoftwareId": "WSXI",
                "charges": [],
                "attributes": [],
                "shipmentContents": [],
                "packageContents": [],
                "commodities": [],
                "customsOptionDetails": [],
                "specialHandlings": [
                    {
                        "type": "DELIVER_WEEKDAY",
                        "description": "Deliver Weekday",
                        "paymentType": "OTHER"
                    },
                    {
                        "type": "RESIDENTIAL_DELIVERY",
                        "description": "Residential Delivery",
                        "paymentType": "OTHER"
                    }
                ],
                "payments": [
                    {
                        "classification": "TRANSPORTATION",
                        "type": "SHIPPER_ACCOUNT",
                        "description": "Shipper"
                    },
                    {
                        "classification": "DUTIES_AND_TAXES",
                        "type": "SHIPPER_ACCOUNT",
                        "description": "Shipper"
                    }
                ],
                "shipperAddress": {
                    "streetLines": [],
                    "city": "Bangalore",
                    "stateOrProvinceCode": "KA",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "datesOrTimes": [
                    {
                        "type": "ACTUAL_DELIVERY",
                        "dateOrTimestamp": "2020-03-18T12:09:00+05:30"
                    },
                    {
                        "type": "ACTUAL_PICKUP",
                        "dateOrTimestamp": "2020-03-16T15:44:00+05:30"
                    },
                    {
                        "type": "SHIP",
                        "dateOrTimestamp": "2020-03-16T00:00:00"
                    },
                    {
                        "type": "ACTUAL_TENDER",
                        "dateOrTimestamp": "2020-03-16T15:44:00+05:30"
                    }
                ],
                "specialInstructions": [],
                "lastUpdatedDestinationAddress": {
                    "streetLines": [],
                    "city": "MUMBAI",
                    "stateOrProvinceCode": "MH",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "destinationAddress": {
                    "streetLines": [],
                    "city": "Mumbai",
                    "stateOrProvinceCode": "MH",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "actualDeliveryAddress": {
                    "streetLines": [],
                    "city": "Mumbai",
                    "stateOrProvinceCode": "MH",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "deliveryLocationType": "RESIDENCE",
                "deliveryLocationDescription": "Residence",
                "deliveryAttempts": 0,
                "deliverySignatureName": "A.GANGULY",
                "pieceCountVerificationDetails": [],
                "totalUniqueAddressCountInConsolidation": 0,
                "availableImages": [
                    {
                        "type": "SIGNATURE_PROOF_OF_DELIVERY"
                    }
                ],
                "notificationEventsAvailable": [
                    "ON_DELIVERY"
                ],
                "splitShipmentParts": [],
                "deliveryOptionEligibilityDetails": [
                    {
                        "option": "INDIRECT_SIGNATURE_RELEASE",
                        "eligibility": "INELIGIBLE"
                    },
                    {
                        "option": "REDIRECT_TO_HOLD_AT_LOCATION",
                        "eligibility": "INELIGIBLE"
                    },
                    {
                        "option": "REROUTE",
                        "eligibility": "INELIGIBLE"
                    },
                    {
                        "option": "RESCHEDULE",
                        "eligibility": "INELIGIBLE"
                    }
                ],
                "events": [
                    {
                        "timestamp": {
                            "$numberLong": "1584513540000"
                        },
                        "eventType": "DL",
                        "eventDescription": "Delivered",
                        "address": {
                            "streetLines": [],
                            "city": "Mumbai",
                            "stateOrProvinceCode": "MH",
                            "postalCode": "400052",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "DELIVERY_LOCATION"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1584506400000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "statusExceptionCode": "67",
                        "statusExceptionDescription": "Tendered to authorized agent for final delivery",
                        "address": {
                            "streetLines": [],
                            "city": "MUMBAI",
                            "stateOrProvinceCode": "MH",
                            "postalCode": "400053",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1584499860000"
                        },
                        "eventType": "AR",
                        "eventDescription": "At local FedEx facility",
                        "address": {
                            "streetLines": [],
                            "city": "MUMBAI",
                            "stateOrProvinceCode": "MH",
                            "postalCode": "400053",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "DESTINATION_FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1584491220000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "BHIWANDI",
                            "stateOrProvinceCode": "MH",
                            "postalCode": "421302",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1584486480000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "BHIWANDI",
                            "stateOrProvinceCode": "MH",
                            "postalCode": "421302",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1584390600000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "562123",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1584383760000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "562123",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1584379440000"
                        },
                        "eventType": "DP",
                        "eventDescription": "Left FedEx origin facility",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "560048",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "ORIGIN_FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1584353640000"
                        },
                        "eventType": "PU",
                        "eventDescription": "Picked up",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "560048",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "PICKUP_LOCATION"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1584348646000"
                        },
                        "eventType": "OC",
                        "eventDescription": "Shipment information sent to FedEx",
                        "address": {
                            "streetLines": [],
                            "residential": False
                        },
                        "arrivalLocation": "CUSTOMER"
                    }
                ]
            }
        ]
    },
    {
        "highestSeverity": "SUCCESS",
        "notifications": [
            {
                "severity": "SUCCESS",
                "source": "trck",
                "code": "0",
                "message": "Request was successfully processed.",
                "localizedMessage": "Request was successfully processed.",
                "messageParameters": []
            }
        ],
        "duplicateWaybill": False,
        "moreData": False,
        "trackDetailsCount": 0,
        "trackDetails": [
            {
                "notification": {
                    "severity": "SUCCESS",
                    "source": "trck",
                    "code": "0",
                    "message": "Request was successfully processed.",
                    "localizedMessage": "Request was successfully processed.",
                    "messageParameters": []
                },
                "trackingNumber": "390807994538",
                "trackingNumberUniqueIdentifier": "2458912000~390807994538~FX",
                "statusDetail": {
                    "creationTime": {
                        "$numberLong": "1583539200000"
                    },
                    "code": "DL",
                    "description": "Delivered",
                    "location": {
                        "streetLines": [],
                        "city": "New Delhi",
                        "stateOrProvinceCode": "DL",
                        "countryCode": "IN",
                        "countryName": "India",
                        "residential": False
                    },
                    "ancillaryDetails": []
                },
                "informationNotes": [],
                "customerExceptionRequests": [],
                "carrierCode": "FDXE",
                "operatingCompanyOrCarrierDescription": "FedEx Express",
                "otherIdentifiers": [],
                "service": {
                    "type": "FEDEX_EXPRESS_SAVER",
                    "description": "FedEx Economy",
                    "shortDescription": "XS"
                },
                "packageWeight": {
                    "units": "KG",
                    "value": 14
                },
                "shipmentWeight": {
                    "units": "KG",
                    "value": 14
                },
                "packaging": {
                    "type": "YOUR_PACKAGING",
                    "description": "Your Packaging"
                },
                "packageSequenceNumber": 1,
                "packageCount": 1,
                "shipmentContentPieceCount": 0,
                "packageContentPieceCount": 0,
                "creatorSoftwareId": "WSXI",
                "charges": [],
                "attributes": [],
                "shipmentContents": [],
                "packageContents": [],
                "commodities": [],
                "customsOptionDetails": [],
                "specialHandlings": [
                    {
                        "type": "DELIVER_WEEKDAY",
                        "description": "Deliver Weekday",
                        "paymentType": "OTHER"
                    },
                    {
                        "type": "RESIDENTIAL_DELIVERY",
                        "description": "Residential Delivery",
                        "paymentType": "OTHER"
                    }
                ],
                "payments": [
                    {
                        "classification": "TRANSPORTATION",
                        "type": "SHIPPER_ACCOUNT",
                        "description": "Shipper"
                    },
                    {
                        "classification": "DUTIES_AND_TAXES",
                        "type": "SHIPPER_ACCOUNT",
                        "description": "Shipper"
                    }
                ],
                "shipperAddress": {
                    "streetLines": [],
                    "city": "Bangalore",
                    "stateOrProvinceCode": "KA",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "datesOrTimes": [
                    {
                        "type": "ACTUAL_DELIVERY",
                        "dateOrTimestamp": "2020-03-07T15:19:00+05:30"
                    },
                    {
                        "type": "ACTUAL_PICKUP",
                        "dateOrTimestamp": "2020-03-03T16:19:00+05:30"
                    },
                    {
                        "type": "SHIP",
                        "dateOrTimestamp": "2020-03-03T00:00:00"
                    },
                    {
                        "type": "ACTUAL_TENDER",
                        "dateOrTimestamp": "2020-03-03T16:19:00+05:30"
                    }
                ],
                "specialInstructions": [],
                "lastUpdatedDestinationAddress": {
                    "streetLines": [],
                    "city": "NEW DELHI",
                    "stateOrProvinceCode": "DL",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "destinationAddress": {
                    "streetLines": [],
                    "city": "New Delhi",
                    "stateOrProvinceCode": "DL",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "actualDeliveryAddress": {
                    "streetLines": [],
                    "city": "New Delhi",
                    "stateOrProvinceCode": "DL",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "deliveryLocationType": "RESIDENCE",
                "deliveryLocationDescription": "Residence",
                "deliveryAttempts": 0,
                "deliverySignatureName": "S.SALONI",
                "pieceCountVerificationDetails": [],
                "totalUniqueAddressCountInConsolidation": 0,
                "availableImages": [
                    {
                        "type": "SIGNATURE_PROOF_OF_DELIVERY"
                    }
                ],
                "notificationEventsAvailable": [
                    "ON_DELIVERY"
                ],
                "splitShipmentParts": [],
                "deliveryOptionEligibilityDetails": [
                    {
                        "option": "INDIRECT_SIGNATURE_RELEASE",
                        "eligibility": "INELIGIBLE"
                    },
                    {
                        "option": "REDIRECT_TO_HOLD_AT_LOCATION",
                        "eligibility": "INELIGIBLE"
                    },
                    {
                        "option": "REROUTE",
                        "eligibility": "INELIGIBLE"
                    },
                    {
                        "option": "RESCHEDULE",
                        "eligibility": "INELIGIBLE"
                    }
                ],
                "events": [
                    {
                        "timestamp": {
                            "$numberLong": "1583574540000"
                        },
                        "eventType": "DL",
                        "eventDescription": "Delivered",
                        "address": {
                            "streetLines": [],
                            "city": "New Delhi",
                            "stateOrProvinceCode": "DL",
                            "postalCode": "110087",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "DELIVERY_LOCATION"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583556780000"
                        },
                        "eventType": "OD",
                        "eventDescription": "On FedEx vehicle for delivery",
                        "address": {
                            "streetLines": [],
                            "city": "NEW DELHI",
                            "stateOrProvinceCode": "DL",
                            "postalCode": "110042",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "VEHICLE"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583553600000"
                        },
                        "eventType": "AR",
                        "eventDescription": "At local FedEx facility",
                        "address": {
                            "streetLines": [],
                            "city": "NEW DELHI",
                            "stateOrProvinceCode": "DL",
                            "postalCode": "110042",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "DESTINATION_FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583535480000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "GURGAON",
                            "stateOrProvinceCode": "HR",
                            "postalCode": "122001",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583522640000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "GURGAON",
                            "stateOrProvinceCode": "HR",
                            "postalCode": "122001",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583521920000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "GURGAON",
                            "stateOrProvinceCode": "HR",
                            "postalCode": "122001",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583277180000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "562123",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583259780000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "562123",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583232540000"
                        },
                        "eventType": "PU",
                        "eventDescription": "Picked up",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "560048",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "PICKUP_LOCATION"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583219141000"
                        },
                        "eventType": "OC",
                        "eventDescription": "Shipment information sent to FedEx",
                        "address": {
                            "streetLines": [],
                            "residential": False
                        },
                        "arrivalLocation": "CUSTOMER"
                    }
                ]
            }
        ]
    },
    {
        "highestSeverity": "SUCCESS",
        "notifications": [
            {
                "severity": "SUCCESS",
                "source": "trck",
                "code": "0",
                "message": "Request was successfully processed.",
                "localizedMessage": "Request was successfully processed.",
                "messageParameters": []
            }
        ],
        "duplicateWaybill": False,
        "moreData": False,
        "trackDetailsCount": 0,
        "trackDetails": [
            {
                "notification": {
                    "severity": "SUCCESS",
                    "source": "trck",
                    "code": "0",
                    "message": "Request was successfully processed.",
                    "localizedMessage": "Request was successfully processed.",
                    "messageParameters": []
                },
                "trackingNumber": "390950134073",
                "trackingNumberUniqueIdentifier": "2458918000~390950134073~FX",
                "statusDetail": {
                    "creationTime": {
                        "$numberLong": "1584057600000"
                    },
                    "code": "DL",
                    "description": "Delivered",
                    "location": {
                        "streetLines": [],
                        "city": "Delhi",
                        "stateOrProvinceCode": "DL",
                        "countryCode": "IN",
                        "countryName": "India",
                        "residential": False
                    },
                    "ancillaryDetails": []
                },
                "informationNotes": [],
                "customerExceptionRequests": [],
                "carrierCode": "FDXE",
                "operatingCompanyOrCarrierDescription": "FedEx Express",
                "otherIdentifiers": [],
                "service": {
                    "type": "FEDEX_EXPRESS_SAVER",
                    "description": "FedEx Economy",
                    "shortDescription": "XS"
                },
                "packageWeight": {
                    "units": "KG",
                    "value": 14
                },
                "packageDimensions": {
                    "length": 38,
                    "width": 25,
                    "height": 61,
                    "units": "CM"
                },
                "shipmentWeight": {
                    "units": "KG",
                    "value": 14
                },
                "packaging": {
                    "type": "YOUR_PACKAGING",
                    "description": "Your Packaging"
                },
                "packageSequenceNumber": 1,
                "packageCount": 1,
                "shipmentContentPieceCount": 0,
                "packageContentPieceCount": 0,
                "creatorSoftwareId": "WSXI",
                "charges": [],
                "attributes": [],
                "shipmentContents": [],
                "packageContents": [],
                "commodities": [],
                "customsOptionDetails": [],
                "specialHandlings": [
                    {
                        "type": "DELIVER_WEEKDAY",
                        "description": "Deliver Weekday",
                        "paymentType": "OTHER"
                    },
                    {
                        "type": "COD",
                        "description": "Collect On Delivery (COD)",
                        "paymentType": "OTHER"
                    },
                    {
                        "type": "RESIDENTIAL_DELIVERY",
                        "description": "Residential Delivery",
                        "paymentType": "OTHER"
                    }
                ],
                "payments": [
                    {
                        "classification": "TRANSPORTATION",
                        "type": "SHIPPER_ACCOUNT",
                        "description": "Shipper"
                    },
                    {
                        "classification": "DUTIES_AND_TAXES",
                        "type": "SHIPPER_ACCOUNT",
                        "description": "Shipper"
                    }
                ],
                "shipperAddress": {
                    "streetLines": [],
                    "city": "Bangalore",
                    "stateOrProvinceCode": "KA",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "datesOrTimes": [
                    {
                        "type": "ACTUAL_DELIVERY",
                        "dateOrTimestamp": "2020-03-13T14:44:00+05:30"
                    },
                    {
                        "type": "ACTUAL_PICKUP",
                        "dateOrTimestamp": "2020-03-09T15:12:00+05:30"
                    },
                    {
                        "type": "SHIP",
                        "dateOrTimestamp": "2020-03-09T00:00:00"
                    },
                    {
                        "type": "ACTUAL_TENDER",
                        "dateOrTimestamp": "2020-03-09T15:12:00+05:30"
                    }
                ],
                "specialInstructions": [],
                "lastUpdatedDestinationAddress": {
                    "streetLines": [],
                    "city": "DELHI",
                    "stateOrProvinceCode": "DL",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "destinationAddress": {
                    "streetLines": [],
                    "city": "Delhi",
                    "stateOrProvinceCode": "DL",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "actualDeliveryAddress": {
                    "streetLines": [],
                    "city": "Delhi",
                    "stateOrProvinceCode": "DL",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "deliveryLocationType": "RESIDENCE",
                "deliveryLocationDescription": "Residence",
                "deliveryAttempts": 0,
                "deliverySignatureName": "M.MOHIT",
                "pieceCountVerificationDetails": [],
                "totalUniqueAddressCountInConsolidation": 0,
                "availableImages": [
                    {
                        "type": "SIGNATURE_PROOF_OF_DELIVERY"
                    }
                ],
                "notificationEventsAvailable": [
                    "ON_DELIVERY"
                ],
                "splitShipmentParts": [],
                "deliveryOptionEligibilityDetails": [
                    {
                        "option": "INDIRECT_SIGNATURE_RELEASE",
                        "eligibility": "INELIGIBLE"
                    },
                    {
                        "option": "REDIRECT_TO_HOLD_AT_LOCATION",
                        "eligibility": "INELIGIBLE"
                    },
                    {
                        "option": "REROUTE",
                        "eligibility": "INELIGIBLE"
                    },
                    {
                        "option": "RESCHEDULE",
                        "eligibility": "INELIGIBLE"
                    }
                ],
                "events": [
                    {
                        "timestamp": {
                            "$numberLong": "1584090840000"
                        },
                        "eventType": "DL",
                        "eventDescription": "Delivered",
                        "address": {
                            "streetLines": [],
                            "city": "Delhi",
                            "stateOrProvinceCode": "DL",
                            "postalCode": "110009",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "DELIVERY_LOCATION"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1584072120000"
                        },
                        "eventType": "OD",
                        "eventDescription": "On FedEx vehicle for delivery",
                        "address": {
                            "streetLines": [],
                            "city": "NEW DELHI",
                            "stateOrProvinceCode": "DL",
                            "postalCode": "110042",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "VEHICLE"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1584071820000"
                        },
                        "eventType": "AR",
                        "eventDescription": "At local FedEx facility",
                        "address": {
                            "streetLines": [],
                            "city": "NEW DELHI",
                            "stateOrProvinceCode": "DL",
                            "postalCode": "110042",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "DESTINATION_FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1584052680000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "GURGAON",
                            "stateOrProvinceCode": "HR",
                            "postalCode": "122001",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1584041160000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "GURGAON",
                            "stateOrProvinceCode": "HR",
                            "postalCode": "122001",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583796000000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "562123",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583781180000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "562123",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583773020000"
                        },
                        "eventType": "DP",
                        "eventDescription": "Left FedEx origin facility",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "560048",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "ORIGIN_FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583746920000"
                        },
                        "eventType": "PU",
                        "eventDescription": "Picked up",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "560048",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "PICKUP_LOCATION"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583742792000"
                        },
                        "eventType": "OC",
                        "eventDescription": "Shipment information sent to FedEx",
                        "address": {
                            "streetLines": [],
                            "residential": False
                        },
                        "arrivalLocation": "CUSTOMER"
                    }
                ]
            }
        ]
    },
    {
        "highestSeverity": "SUCCESS",
        "notifications": [
            {
                "severity": "SUCCESS",
                "source": "trck",
                "code": "0",
                "message": "Request was successfully processed.",
                "localizedMessage": "Request was successfully processed.",
                "messageParameters": []
            }
        ],
        "duplicateWaybill": False,
        "moreData": False,
        "trackDetailsCount": 0,
        "trackDetails": [
            {
                "notification": {
                    "severity": "SUCCESS",
                    "source": "trck",
                    "code": "0",
                    "message": "Request was successfully processed.",
                    "localizedMessage": "Request was successfully processed.",
                    "messageParameters": []
                },
                "trackingNumber": "390950572730",
                "trackingNumberUniqueIdentifier": "2458918000~390950572730~FX",
                "statusDetail": {
                    "creationTime": {
                        "$numberLong": "1583798400000"
                    },
                    "code": "DL",
                    "description": "Delivered",
                    "location": {
                        "streetLines": [],
                        "city": "Bangalore",
                        "stateOrProvinceCode": "KA",
                        "countryCode": "IN",
                        "countryName": "India",
                        "residential": False
                    },
                    "ancillaryDetails": []
                },
                "informationNotes": [],
                "customerExceptionRequests": [],
                "carrierCode": "FDXE",
                "operatingCompanyOrCarrierDescription": "FedEx Express",
                "otherIdentifiers": [],
                "service": {
                    "type": "FEDEX_EXPRESS_SAVER",
                    "description": "FedEx Economy",
                    "shortDescription": "XS"
                },
                "packageWeight": {
                    "units": "KG",
                    "value": 28
                },
                "shipmentWeight": {
                    "units": "KG",
                    "value": 28
                },
                "packaging": {
                    "type": "YOUR_PACKAGING",
                    "description": "Your Packaging"
                },
                "packageSequenceNumber": 1,
                "packageCount": 1,
                "shipmentContentPieceCount": 0,
                "packageContentPieceCount": 0,
                "creatorSoftwareId": "WSXI",
                "charges": [],
                "attributes": [],
                "shipmentContents": [],
                "packageContents": [],
                "commodities": [],
                "customsOptionDetails": [],
                "specialHandlings": [
                    {
                        "type": "DELIVER_WEEKDAY",
                        "description": "Deliver Weekday",
                        "paymentType": "OTHER"
                    }
                ],
                "payments": [
                    {
                        "classification": "TRANSPORTATION",
                        "type": "SHIPPER_ACCOUNT",
                        "description": "Shipper"
                    },
                    {
                        "classification": "DUTIES_AND_TAXES",
                        "type": "SHIPPER_ACCOUNT",
                        "description": "Shipper"
                    }
                ],
                "shipperAddress": {
                    "streetLines": [],
                    "city": "Bangalore",
                    "stateOrProvinceCode": "KA",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "datesOrTimes": [
                    {
                        "type": "ACTUAL_DELIVERY",
                        "dateOrTimestamp": "2020-03-10T15:30:00+05:30"
                    },
                    {
                        "type": "ACTUAL_PICKUP",
                        "dateOrTimestamp": "2020-03-09T15:12:00+05:30"
                    },
                    {
                        "type": "SHIP",
                        "dateOrTimestamp": "2020-03-09T00:00:00"
                    },
                    {
                        "type": "ACTUAL_TENDER",
                        "dateOrTimestamp": "2020-03-09T15:12:00+05:30"
                    }
                ],
                "specialInstructions": [],
                "lastUpdatedDestinationAddress": {
                    "streetLines": [],
                    "city": "BANGALORE",
                    "stateOrProvinceCode": "KA",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "destinationAddress": {
                    "streetLines": [],
                    "city": "Bangalore",
                    "stateOrProvinceCode": "KA",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "actualDeliveryAddress": {
                    "streetLines": [],
                    "city": "Bangalore",
                    "stateOrProvinceCode": "KA",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "deliveryLocationType": "RECEPTIONIST_OR_FRONT_DESK",
                "deliveryLocationDescription": "Receptionist/Front Desk",
                "deliveryAttempts": 0,
                "deliverySignatureName": "A.AMAR",
                "pieceCountVerificationDetails": [],
                "totalUniqueAddressCountInConsolidation": 0,
                "availableImages": [
                    {
                        "type": "SIGNATURE_PROOF_OF_DELIVERY"
                    }
                ],
                "notificationEventsAvailable": [
                    "ON_DELIVERY"
                ],
                "splitShipmentParts": [],
                "deliveryOptionEligibilityDetails": [
                    {
                        "option": "INDIRECT_SIGNATURE_RELEASE",
                        "eligibility": "INELIGIBLE"
                    },
                    {
                        "option": "REDIRECT_TO_HOLD_AT_LOCATION",
                        "eligibility": "INELIGIBLE"
                    },
                    {
                        "option": "REROUTE",
                        "eligibility": "INELIGIBLE"
                    },
                    {
                        "option": "RESCHEDULE",
                        "eligibility": "INELIGIBLE"
                    }
                ],
                "events": [
                    {
                        "timestamp": {
                            "$numberLong": "1583834400000"
                        },
                        "eventType": "DL",
                        "eventDescription": "Delivered",
                        "address": {
                            "streetLines": [],
                            "city": "Bangalore",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "560038",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "DELIVERY_LOCATION"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583813700000"
                        },
                        "eventType": "OD",
                        "eventDescription": "On FedEx vehicle for delivery",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "560045",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "VEHICLE"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583811900000"
                        },
                        "eventType": "AR",
                        "eventDescription": "At local FedEx facility",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "560045",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "DESTINATION_FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583810400000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "560045",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583802120000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "562123",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583781180000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "562123",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583773020000"
                        },
                        "eventType": "DP",
                        "eventDescription": "Left FedEx origin facility",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "560048",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "ORIGIN_FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583746920000"
                        },
                        "eventType": "PU",
                        "eventDescription": "Picked up",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "560048",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "PICKUP_LOCATION"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583745682000"
                        },
                        "eventType": "OC",
                        "eventDescription": "Shipment information sent to FedEx",
                        "address": {
                            "streetLines": [],
                            "residential": False
                        },
                        "arrivalLocation": "CUSTOMER"
                    }
                ]
            }
        ]
    },
    {
        "highestSeverity": "SUCCESS",
        "notifications": [
            {
                "severity": "SUCCESS",
                "source": "trck",
                "code": "0",
                "message": "Request was successfully processed.",
                "localizedMessage": "Request was successfully processed.",
                "messageParameters": []
            }
        ],
        "duplicateWaybill": False,
        "moreData": False,
        "trackDetailsCount": 0,
        "trackDetails": [
            {
                "notification": {
                    "severity": "SUCCESS",
                    "source": "trck",
                    "code": "0",
                    "message": "Request was successfully processed.",
                    "localizedMessage": "Request was successfully processed.",
                    "messageParameters": []
                },
                "trackingNumber": "390839041400",
                "trackingNumberUniqueIdentifier": "2458913000~390839041400~FX",
                "statusDetail": {
                    "creationTime": {
                        "$numberLong": "1583712000000"
                    },
                    "code": "DL",
                    "description": "Delivered",
                    "location": {
                        "streetLines": [],
                        "city": "Delhi",
                        "stateOrProvinceCode": "DL",
                        "countryCode": "IN",
                        "countryName": "India",
                        "residential": False
                    },
                    "ancillaryDetails": [
                        {
                            "reason": "11",
                            "reasonDescription": "C.O.D. payment received"
                        }
                    ]
                },
                "informationNotes": [],
                "customerExceptionRequests": [],
                "carrierCode": "FDXE",
                "operatingCompanyOrCarrierDescription": "FedEx Express",
                "otherIdentifiers": [
                    {
                        "packageIdentifier": {
                            "type": "COD_RETURN_TRACKING_NUMBER",
                            "value": "132152390141"
                        },
                        "trackingNumberUniqueIdentifier": "2458918000"
                    }
                ],
                "service": {
                    "type": "FEDEX_EXPRESS_SAVER",
                    "description": "FedEx Economy",
                    "shortDescription": "XS"
                },
                "packageWeight": {
                    "units": "KG",
                    "value": 14
                },
                "packageDimensions": {
                    "length": 38,
                    "width": 25,
                    "height": 61,
                    "units": "CM"
                },
                "shipmentWeight": {
                    "units": "KG",
                    "value": 14
                },
                "packaging": {
                    "type": "YOUR_PACKAGING",
                    "description": "Your Packaging"
                },
                "packageSequenceNumber": 1,
                "packageCount": 1,
                "shipmentContentPieceCount": 0,
                "packageContentPieceCount": 0,
                "creatorSoftwareId": "WSXI",
                "charges": [],
                "attributes": [],
                "shipmentContents": [],
                "packageContents": [],
                "commodities": [],
                "customsOptionDetails": [],
                "specialHandlings": [
                    {
                        "type": "DELIVER_WEEKDAY",
                        "description": "Deliver Weekday",
                        "paymentType": "OTHER"
                    },
                    {
                        "type": "COD",
                        "description": "Collect On Delivery (COD)",
                        "paymentType": "OTHER"
                    },
                    {
                        "type": "RESIDENTIAL_DELIVERY",
                        "description": "Residential Delivery",
                        "paymentType": "OTHER"
                    }
                ],
                "payments": [
                    {
                        "classification": "TRANSPORTATION",
                        "type": "SHIPPER_ACCOUNT",
                        "description": "Shipper"
                    },
                    {
                        "classification": "DUTIES_AND_TAXES",
                        "type": "SHIPPER_ACCOUNT",
                        "description": "Shipper"
                    }
                ],
                "shipperAddress": {
                    "streetLines": [],
                    "city": "Bangalore",
                    "stateOrProvinceCode": "KA",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "datesOrTimes": [
                    {
                        "type": "ACTUAL_DELIVERY",
                        "dateOrTimestamp": "2020-03-09T14:45:00+05:30"
                    },
                    {
                        "type": "ACTUAL_PICKUP",
                        "dateOrTimestamp": "2020-03-04T16:13:00+05:30"
                    },
                    {
                        "type": "SHIP",
                        "dateOrTimestamp": "2020-03-04T00:00:00"
                    },
                    {
                        "type": "ACTUAL_TENDER",
                        "dateOrTimestamp": "2020-03-04T16:13:00+05:30"
                    }
                ],
                "specialInstructions": [],
                "lastUpdatedDestinationAddress": {
                    "streetLines": [],
                    "city": "DELHI",
                    "stateOrProvinceCode": "DL",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "destinationAddress": {
                    "streetLines": [],
                    "city": "Delhi",
                    "stateOrProvinceCode": "DL",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "actualDeliveryAddress": {
                    "streetLines": [],
                    "city": "Delhi",
                    "stateOrProvinceCode": "DL",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "deliveryLocationType": "RESIDENCE",
                "deliveryLocationDescription": "Residence",
                "deliveryAttempts": 0,
                "deliverySignatureName": "M.VIPIN",
                "pieceCountVerificationDetails": [],
                "totalUniqueAddressCountInConsolidation": 0,
                "availableImages": [
                    {
                        "type": "SIGNATURE_PROOF_OF_DELIVERY"
                    }
                ],
                "notificationEventsAvailable": [
                    "ON_DELIVERY"
                ],
                "splitShipmentParts": [],
                "deliveryOptionEligibilityDetails": [
                    {
                        "option": "INDIRECT_SIGNATURE_RELEASE",
                        "eligibility": "INELIGIBLE"
                    },
                    {
                        "option": "REDIRECT_TO_HOLD_AT_LOCATION",
                        "eligibility": "INELIGIBLE"
                    },
                    {
                        "option": "REROUTE",
                        "eligibility": "INELIGIBLE"
                    },
                    {
                        "option": "RESCHEDULE",
                        "eligibility": "INELIGIBLE"
                    }
                ],
                "events": [
                    {
                        "timestamp": {
                            "$numberLong": "1583745300000"
                        },
                        "eventType": "DL",
                        "eventDescription": "Delivered",
                        "statusExceptionCode": "11",
                        "statusExceptionDescription": "C.O.D. payment received",
                        "address": {
                            "streetLines": [],
                            "city": "Delhi",
                            "stateOrProvinceCode": "DL",
                            "postalCode": "110027",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "DELIVERY_LOCATION"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583728620000"
                        },
                        "eventType": "OD",
                        "eventDescription": "On FedEx vehicle for delivery",
                        "address": {
                            "streetLines": [],
                            "city": "NEW DELHI",
                            "stateOrProvinceCode": "DL",
                            "postalCode": "110064",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "VEHICLE"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583651940000"
                        },
                        "eventType": "AR",
                        "eventDescription": "At local FedEx facility",
                        "address": {
                            "streetLines": [],
                            "city": "NEW DELHI",
                            "stateOrProvinceCode": "DL",
                            "postalCode": "110064",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "DESTINATION_FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583644320000"
                        },
                        "eventType": "AR",
                        "eventDescription": "At local FedEx facility",
                        "address": {
                            "streetLines": [],
                            "city": "NEW DELHI",
                            "stateOrProvinceCode": "DL",
                            "postalCode": "110064",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "DESTINATION_FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583619840000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "GURGAON",
                            "stateOrProvinceCode": "HR",
                            "postalCode": "122001",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583619780000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "GURGAON",
                            "stateOrProvinceCode": "HR",
                            "postalCode": "122001",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583613060000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "GURGAON",
                            "stateOrProvinceCode": "HR",
                            "postalCode": "122001",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583365200000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "562123",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583354520000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "562123",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583354520000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "562123",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583343060000"
                        },
                        "eventType": "DP",
                        "eventDescription": "Left FedEx origin facility",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "560048",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "ORIGIN_FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583318580000"
                        },
                        "eventType": "PU",
                        "eventDescription": "Picked up",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "560048",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "PICKUP_LOCATION"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583299923000"
                        },
                        "eventType": "OC",
                        "eventDescription": "Shipment information sent to FedEx",
                        "address": {
                            "streetLines": [],
                            "residential": False
                        },
                        "arrivalLocation": "CUSTOMER"
                    }
                ]
            }
        ]
    },
    {
        "highestSeverity": "SUCCESS",
        "notifications": [
            {
                "severity": "SUCCESS",
                "source": "trck",
                "code": "0",
                "message": "Request was successfully processed.",
                "localizedMessage": "Request was successfully processed.",
                "messageParameters": []
            }
        ],
        "duplicateWaybill": False,
        "moreData": False,
        "trackDetailsCount": 0,
        "trackDetails": [
            {
                "notification": {
                    "severity": "SUCCESS",
                    "source": "trck",
                    "code": "0",
                    "message": "Request was successfully processed.",
                    "localizedMessage": "Request was successfully processed.",
                    "messageParameters": []
                },
                "trackingNumber": "390807999654",
                "trackingNumberUniqueIdentifier": "2458912000~390807999654~FX",
                "statusDetail": {
                    "creationTime": {
                        "$numberLong": "1583971200000"
                    },
                    "code": "DL",
                    "description": "Delivered",
                    "location": {
                        "streetLines": [],
                        "city": "Bokaro steel City",
                        "stateOrProvinceCode": "JH",
                        "countryCode": "IN",
                        "countryName": "India",
                        "residential": False
                    },
                    "ancillaryDetails": []
                },
                "informationNotes": [],
                "customerExceptionRequests": [],
                "carrierCode": "FDXE",
                "operatingCompanyOrCarrierDescription": "FedEx Express",
                "otherIdentifiers": [],
                "service": {
                    "type": "FEDEX_EXPRESS_SAVER",
                    "description": "FedEx Economy",
                    "shortDescription": "XS"
                },
                "packageWeight": {
                    "units": "KG",
                    "value": 14
                },
                "shipmentWeight": {
                    "units": "KG",
                    "value": 14
                },
                "packaging": {
                    "type": "YOUR_PACKAGING",
                    "description": "Your Packaging"
                },
                "packageSequenceNumber": 1,
                "packageCount": 1,
                "shipmentContentPieceCount": 0,
                "packageContentPieceCount": 0,
                "creatorSoftwareId": "WSXI",
                "charges": [],
                "attributes": [],
                "shipmentContents": [],
                "packageContents": [],
                "commodities": [],
                "customsOptionDetails": [],
                "specialHandlings": [
                    {
                        "type": "DELIVER_WEEKDAY",
                        "description": "Deliver Weekday",
                        "paymentType": "OTHER"
                    }
                ],
                "payments": [
                    {
                        "classification": "TRANSPORTATION",
                        "type": "SHIPPER_ACCOUNT",
                        "description": "Shipper"
                    },
                    {
                        "classification": "DUTIES_AND_TAXES",
                        "type": "SHIPPER_ACCOUNT",
                        "description": "Shipper"
                    }
                ],
                "shipperAddress": {
                    "streetLines": [],
                    "city": "Bangalore",
                    "stateOrProvinceCode": "KA",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "datesOrTimes": [
                    {
                        "type": "ACTUAL_DELIVERY",
                        "dateOrTimestamp": "2020-03-12T13:00:00+05:30"
                    },
                    {
                        "type": "ACTUAL_PICKUP",
                        "dateOrTimestamp": "2020-03-03T16:19:00+05:30"
                    },
                    {
                        "type": "SHIP",
                        "dateOrTimestamp": "2020-03-03T00:00:00"
                    },
                    {
                        "type": "ACTUAL_TENDER",
                        "dateOrTimestamp": "2020-03-03T16:19:00+05:30"
                    }
                ],
                "specialInstructions": [],
                "lastUpdatedDestinationAddress": {
                    "streetLines": [],
                    "city": "BOKARO STEEL CITY",
                    "stateOrProvinceCode": "JH",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "destinationAddress": {
                    "streetLines": [],
                    "city": "Bokaro steel City",
                    "stateOrProvinceCode": "JH",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "actualDeliveryAddress": {
                    "streetLines": [],
                    "city": "Bokaro steel City",
                    "stateOrProvinceCode": "JH",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "deliveryLocationType": "RECEPTIONIST_OR_FRONT_DESK",
                "deliveryLocationDescription": "Receptionist/Front Desk",
                "deliveryAttempts": 0,
                "deliverySignatureName": "SUNIL KR",
                "pieceCountVerificationDetails": [],
                "totalUniqueAddressCountInConsolidation": 0,
                "availableImages": [],
                "notificationEventsAvailable": [
                    "ON_DELIVERY"
                ],
                "splitShipmentParts": [],
                "deliveryOptionEligibilityDetails": [
                    {
                        "option": "INDIRECT_SIGNATURE_RELEASE",
                        "eligibility": "INELIGIBLE"
                    },
                    {
                        "option": "REDIRECT_TO_HOLD_AT_LOCATION",
                        "eligibility": "INELIGIBLE"
                    },
                    {
                        "option": "REROUTE",
                        "eligibility": "INELIGIBLE"
                    },
                    {
                        "option": "RESCHEDULE",
                        "eligibility": "INELIGIBLE"
                    }
                ],
                "events": [
                    {
                        "timestamp": {
                            "$numberLong": "1583998200000"
                        },
                        "eventType": "DL",
                        "eventDescription": "Delivered",
                        "address": {
                            "streetLines": [],
                            "city": "Bokaro steel City",
                            "stateOrProvinceCode": "JH",
                            "postalCode": "827001",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "DELIVERY_LOCATION"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583992380000"
                        },
                        "eventType": "OD",
                        "eventDescription": "On FedEx vehicle for delivery",
                        "address": {
                            "streetLines": [],
                            "city": "BOKARO",
                            "stateOrProvinceCode": "JH",
                            "postalCode": "827004",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "VEHICLE"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583987040000"
                        },
                        "eventType": "AR",
                        "eventDescription": "At local FedEx facility",
                        "address": {
                            "streetLines": [],
                            "city": "BOKARO",
                            "stateOrProvinceCode": "JH",
                            "postalCode": "827004",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "DESTINATION_FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583929620000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "RANCHI",
                            "stateOrProvinceCode": "JH",
                            "postalCode": "834001",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583633280000"
                        },
                        "eventType": "AR",
                        "eventDescription": "At local FedEx facility",
                        "address": {
                            "streetLines": [],
                            "city": "RANCHI",
                            "stateOrProvinceCode": "JH",
                            "postalCode": "834001",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "DESTINATION_FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583575980000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "BAHARAGORA",
                            "stateOrProvinceCode": "JH",
                            "postalCode": "832101",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583561880000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "BAHARAGORA",
                            "stateOrProvinceCode": "JH",
                            "postalCode": "832101",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583297040000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "562123",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583259780000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "562123",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583232540000"
                        },
                        "eventType": "PU",
                        "eventDescription": "Picked up",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "560048",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "PICKUP_LOCATION"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583219179000"
                        },
                        "eventType": "OC",
                        "eventDescription": "Shipment information sent to FedEx",
                        "address": {
                            "streetLines": [],
                            "residential": False
                        },
                        "arrivalLocation": "CUSTOMER"
                    }
                ]
            }
        ]
    },
    {
        "highestSeverity": "SUCCESS",
        "notifications": [
            {
                "severity": "SUCCESS",
                "source": "trck",
                "code": "0",
                "message": "Request was successfully processed.",
                "localizedMessage": "Request was successfully processed.",
                "messageParameters": []
            }
        ],
        "duplicateWaybill": False,
        "moreData": False,
        "trackDetailsCount": 0,
        "trackDetails": [
            {
                "notification": {
                    "severity": "SUCCESS",
                    "source": "trck",
                    "code": "0",
                    "message": "Request was successfully processed.",
                    "localizedMessage": "Request was successfully processed.",
                    "messageParameters": []
                },
                "trackingNumber": "390767871261",
                "trackingNumberUniqueIdentifier": "2458911000~390767871261~FX",
                "statusDetail": {
                    "creationTime": {
                        "$numberLong": "1583884800000"
                    },
                    "code": "DL",
                    "description": "Delivered",
                    "location": {
                        "streetLines": [],
                        "city": "Gurugram",
                        "stateOrProvinceCode": "HR",
                        "countryCode": "IN",
                        "countryName": "India",
                        "residential": False
                    },
                    "ancillaryDetails": []
                },
                "informationNotes": [],
                "customerExceptionRequests": [],
                "carrierCode": "FDXE",
                "operatingCompanyOrCarrierDescription": "FedEx Express",
                "otherIdentifiers": [],
                "service": {
                    "type": "FEDEX_EXPRESS_SAVER",
                    "description": "FedEx Economy",
                    "shortDescription": "XS"
                },
                "packageWeight": {
                    "units": "KG",
                    "value": 14
                },
                "shipmentWeight": {
                    "units": "KG",
                    "value": 14
                },
                "packaging": {
                    "type": "YOUR_PACKAGING",
                    "description": "Your Packaging"
                },
                "packageSequenceNumber": 1,
                "packageCount": 1,
                "shipmentContentPieceCount": 0,
                "packageContentPieceCount": 0,
                "creatorSoftwareId": "WSXI",
                "charges": [],
                "attributes": [],
                "shipmentContents": [],
                "packageContents": [],
                "commodities": [],
                "customsOptionDetails": [],
                "specialHandlings": [
                    {
                        "type": "DELIVER_WEEKDAY",
                        "description": "Deliver Weekday",
                        "paymentType": "OTHER"
                    }
                ],
                "payments": [
                    {
                        "classification": "TRANSPORTATION",
                        "type": "SHIPPER_ACCOUNT",
                        "description": "Shipper"
                    },
                    {
                        "classification": "DUTIES_AND_TAXES",
                        "type": "SHIPPER_ACCOUNT",
                        "description": "Shipper"
                    }
                ],
                "shipperAddress": {
                    "streetLines": [],
                    "city": "Bangalore",
                    "stateOrProvinceCode": "KA",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "datesOrTimes": [
                    {
                        "type": "ACTUAL_DELIVERY",
                        "dateOrTimestamp": "2020-03-11T18:30:00+05:30"
                    },
                    {
                        "type": "ACTUAL_PICKUP",
                        "dateOrTimestamp": "2020-03-02T16:23:00+05:30"
                    },
                    {
                        "type": "SHIP",
                        "dateOrTimestamp": "2020-03-02T00:00:00"
                    },
                    {
                        "type": "ACTUAL_TENDER",
                        "dateOrTimestamp": "2020-03-02T16:23:00+05:30"
                    },
                    {
                        "type": "ESTIMATED_RETURN_TO_STATION",
                        "dateOrTimestamp": "2020-03-07T20:00:00+05:30"
                    }
                ],
                "specialInstructions": [],
                "lastUpdatedDestinationAddress": {
                    "streetLines": [],
                    "city": "GURUGRAM",
                    "stateOrProvinceCode": "HR",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "destinationAddress": {
                    "streetLines": [],
                    "city": "Gurugram",
                    "stateOrProvinceCode": "HR",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "actualDeliveryAddress": {
                    "streetLines": [],
                    "city": "Gurugram",
                    "stateOrProvinceCode": "HR",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "deliveryLocationType": "RECEPTIONIST_OR_FRONT_DESK",
                "deliveryLocationDescription": "Receptionist/Front Desk",
                "deliveryAttempts": 0,
                "deliverySignatureName": "SIGN",
                "pieceCountVerificationDetails": [],
                "totalUniqueAddressCountInConsolidation": 0,
                "availableImages": [],
                "notificationEventsAvailable": [
                    "ON_DELIVERY"
                ],
                "splitShipmentParts": [],
                "deliveryOptionEligibilityDetails": [
                    {
                        "option": "INDIRECT_SIGNATURE_RELEASE",
                        "eligibility": "INELIGIBLE"
                    },
                    {
                        "option": "REDIRECT_TO_HOLD_AT_LOCATION",
                        "eligibility": "INELIGIBLE"
                    },
                    {
                        "option": "REROUTE",
                        "eligibility": "INELIGIBLE"
                    },
                    {
                        "option": "RESCHEDULE",
                        "eligibility": "INELIGIBLE"
                    }
                ],
                "events": [
                    {
                        "timestamp": {
                            "$numberLong": "1583931600000"
                        },
                        "eventType": "DL",
                        "eventDescription": "Delivered",
                        "address": {
                            "streetLines": [],
                            "city": "Gurugram",
                            "stateOrProvinceCode": "HR",
                            "postalCode": "122001",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "DELIVERY_LOCATION"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583748720000"
                        },
                        "eventType": "AF",
                        "eventDescription": "At local FedEx facility",
                        "address": {
                            "streetLines": [],
                            "city": "MANESAR",
                            "stateOrProvinceCode": "HR",
                            "postalCode": "122050",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583590800000"
                        },
                        "eventType": "AF",
                        "eventDescription": "At local FedEx facility",
                        "address": {
                            "streetLines": [],
                            "city": "MANESAR",
                            "stateOrProvinceCode": "HR",
                            "postalCode": "122050",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583586000000"
                        },
                        "eventType": "DE",
                        "eventDescription": "Delivery exception",
                        "statusExceptionCode": "17",
                        "statusExceptionDescription": "Future delivery requested",
                        "address": {
                            "streetLines": [],
                            "city": "MANESAR",
                            "stateOrProvinceCode": "HR",
                            "postalCode": "122050",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "DELIVERY_LOCATION"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583563260000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "statusExceptionCode": "67",
                        "statusExceptionDescription": "Tendered to authorized agent for final delivery",
                        "address": {
                            "streetLines": [],
                            "city": "MANESAR",
                            "stateOrProvinceCode": "HR",
                            "postalCode": "122050",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583556480000"
                        },
                        "eventType": "OD",
                        "eventDescription": "On FedEx vehicle for delivery",
                        "address": {
                            "streetLines": [],
                            "city": "MANESAR",
                            "stateOrProvinceCode": "HR",
                            "postalCode": "122050",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "VEHICLE"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583556480000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "statusExceptionCode": "67",
                        "statusExceptionDescription": "Tendered to authorized agent for final delivery",
                        "address": {
                            "streetLines": [],
                            "city": "MANESAR",
                            "stateOrProvinceCode": "HR",
                            "postalCode": "122050",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583510880000"
                        },
                        "eventType": "AF",
                        "eventDescription": "At local FedEx facility",
                        "address": {
                            "streetLines": [],
                            "city": "MANESAR",
                            "stateOrProvinceCode": "HR",
                            "postalCode": "122050",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583499600000"
                        },
                        "eventType": "DE",
                        "eventDescription": "Delivery exception",
                        "statusExceptionCode": "03",
                        "statusExceptionDescription": "Incorrect address",
                        "address": {
                            "streetLines": [],
                            "city": "MANESAR",
                            "stateOrProvinceCode": "HR",
                            "postalCode": "122050",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "DELIVERY_LOCATION"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583455380000"
                        },
                        "eventType": "AR",
                        "eventDescription": "At local FedEx facility",
                        "address": {
                            "streetLines": [],
                            "city": "MANESAR",
                            "stateOrProvinceCode": "HR",
                            "postalCode": "122050",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "DESTINATION_FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583450520000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "GURGAON",
                            "stateOrProvinceCode": "HR",
                            "postalCode": "122001",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583436420000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "GURGAON",
                            "stateOrProvinceCode": "HR",
                            "postalCode": "122001",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583193120000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "562123",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583176260000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "562123",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583176260000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "562123",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583146380000"
                        },
                        "eventType": "PU",
                        "eventDescription": "Picked up",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "560048",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "PICKUP_LOCATION"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583132240000"
                        },
                        "eventType": "OC",
                        "eventDescription": "Shipment information sent to FedEx",
                        "address": {
                            "streetLines": [],
                            "residential": False
                        },
                        "arrivalLocation": "CUSTOMER"
                    }
                ]
            }
        ]
    },
    {
        "highestSeverity": "SUCCESS",
        "notifications": [
            {
                "severity": "SUCCESS",
                "source": "trck",
                "code": "0",
                "message": "Request was successfully processed.",
                "localizedMessage": "Request was successfully processed.",
                "messageParameters": []
            }
        ],
        "duplicateWaybill": False,
        "moreData": False,
        "trackDetailsCount": 0,
        "trackDetails": [
            {
                "notification": {
                    "severity": "SUCCESS",
                    "source": "trck",
                    "code": "0",
                    "message": "Request was successfully processed.",
                    "localizedMessage": "Request was successfully processed.",
                    "messageParameters": []
                },
                "trackingNumber": "391018702750",
                "trackingNumberUniqueIdentifier": "2458920000~391018702750~FX",
                "statusDetail": {
                    "creationTime": {
                        "$numberLong": "1584489600000"
                    },
                    "code": "DL",
                    "description": "Delivered",
                    "location": {
                        "streetLines": [],
                        "city": "Lucknow",
                        "stateOrProvinceCode": "UP",
                        "countryCode": "IN",
                        "countryName": "India",
                        "residential": False
                    },
                    "ancillaryDetails": []
                },
                "informationNotes": [],
                "customerExceptionRequests": [],
                "carrierCode": "FDXE",
                "operatingCompanyOrCarrierDescription": "FedEx Express",
                "otherIdentifiers": [],
                "service": {
                    "type": "FEDEX_EXPRESS_SAVER",
                    "description": "FedEx Economy",
                    "shortDescription": "XS"
                },
                "packageWeight": {
                    "units": "KG",
                    "value": 14
                },
                "packageDimensions": {
                    "length": 38,
                    "width": 25,
                    "height": 61,
                    "units": "CM"
                },
                "shipmentWeight": {
                    "units": "KG",
                    "value": 14
                },
                "packaging": {
                    "type": "YOUR_PACKAGING",
                    "description": "Your Packaging"
                },
                "packageSequenceNumber": 1,
                "packageCount": 1,
                "shipmentContentPieceCount": 0,
                "packageContentPieceCount": 0,
                "creatorSoftwareId": "WSXI",
                "charges": [],
                "attributes": [],
                "shipmentContents": [],
                "packageContents": [],
                "commodities": [],
                "customsOptionDetails": [],
                "specialHandlings": [
                    {
                        "type": "DELIVER_WEEKDAY",
                        "description": "Deliver Weekday",
                        "paymentType": "OTHER"
                    },
                    {
                        "type": "RESIDENTIAL_DELIVERY",
                        "description": "Residential Delivery",
                        "paymentType": "OTHER"
                    }
                ],
                "payments": [
                    {
                        "classification": "TRANSPORTATION",
                        "type": "SHIPPER_ACCOUNT",
                        "description": "Shipper"
                    },
                    {
                        "classification": "DUTIES_AND_TAXES",
                        "type": "SHIPPER_ACCOUNT",
                        "description": "Shipper"
                    }
                ],
                "shipperAddress": {
                    "streetLines": [],
                    "city": "Bangalore",
                    "stateOrProvinceCode": "KA",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "datesOrTimes": [
                    {
                        "type": "ACTUAL_DELIVERY",
                        "dateOrTimestamp": "2020-03-18T19:26:00+05:30"
                    },
                    {
                        "type": "ACTUAL_PICKUP",
                        "dateOrTimestamp": "2020-03-11T16:39:00+05:30"
                    },
                    {
                        "type": "SHIP",
                        "dateOrTimestamp": "2020-03-11T00:00:00"
                    },
                    {
                        "type": "ACTUAL_TENDER",
                        "dateOrTimestamp": "2020-03-11T16:39:00+05:30"
                    }
                ],
                "specialInstructions": [],
                "lastUpdatedDestinationAddress": {
                    "streetLines": [],
                    "city": "LUCKNOW",
                    "stateOrProvinceCode": "UP",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "destinationAddress": {
                    "streetLines": [],
                    "city": "Lucknow",
                    "stateOrProvinceCode": "UP",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "actualDeliveryAddress": {
                    "streetLines": [],
                    "city": "Lucknow",
                    "stateOrProvinceCode": "UP",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "deliveryLocationType": "RESIDENCE",
                "deliveryLocationDescription": "Residence",
                "deliveryAttempts": 0,
                "deliverySignatureName": "A.KUMAR",
                "pieceCountVerificationDetails": [],
                "totalUniqueAddressCountInConsolidation": 0,
                "availableImages": [
                    {
                        "type": "SIGNATURE_PROOF_OF_DELIVERY"
                    }
                ],
                "notificationEventsAvailable": [
                    "ON_DELIVERY"
                ],
                "splitShipmentParts": [],
                "deliveryOptionEligibilityDetails": [
                    {
                        "option": "INDIRECT_SIGNATURE_RELEASE",
                        "eligibility": "INELIGIBLE"
                    },
                    {
                        "option": "REDIRECT_TO_HOLD_AT_LOCATION",
                        "eligibility": "INELIGIBLE"
                    },
                    {
                        "option": "REROUTE",
                        "eligibility": "INELIGIBLE"
                    },
                    {
                        "option": "RESCHEDULE",
                        "eligibility": "INELIGIBLE"
                    }
                ],
                "events": [
                    {
                        "timestamp": {
                            "$numberLong": "1584539760000"
                        },
                        "eventType": "DL",
                        "eventDescription": "Delivered",
                        "address": {
                            "streetLines": [],
                            "city": "Lucknow",
                            "stateOrProvinceCode": "UP",
                            "postalCode": "226010",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "DELIVERY_LOCATION"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1584509400000"
                        },
                        "eventType": "OD",
                        "eventDescription": "On FedEx vehicle for delivery",
                        "address": {
                            "streetLines": [],
                            "city": "LUCKNOW",
                            "stateOrProvinceCode": "UP",
                            "postalCode": "226012",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "VEHICLE"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1584446580000"
                        },
                        "eventType": "DE",
                        "eventDescription": "Delivery exception",
                        "statusExceptionCode": "31",
                        "statusExceptionDescription": "Package at station, arrived after courier dispatch",
                        "address": {
                            "streetLines": [],
                            "city": "LUCKNOW",
                            "stateOrProvinceCode": "UP",
                            "postalCode": "226012",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "DESTINATION_FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1584446580000"
                        },
                        "eventType": "AR",
                        "eventDescription": "At local FedEx facility",
                        "address": {
                            "streetLines": [],
                            "city": "LUCKNOW",
                            "stateOrProvinceCode": "UP",
                            "postalCode": "226012",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "DESTINATION_FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1584446520000"
                        },
                        "eventType": "AR",
                        "eventDescription": "At local FedEx facility",
                        "address": {
                            "streetLines": [],
                            "city": "LUCKNOW",
                            "stateOrProvinceCode": "UP",
                            "postalCode": "226012",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "DESTINATION_FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1584248040000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "GURGAON",
                            "stateOrProvinceCode": "HR",
                            "postalCode": "122001",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1584209040000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "GURGAON",
                            "stateOrProvinceCode": "HR",
                            "postalCode": "122001",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1584200520000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "GURGAON",
                            "stateOrProvinceCode": "HR",
                            "postalCode": "122001",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583969160000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "562123",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583951940000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "562123",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583947800000"
                        },
                        "eventType": "DP",
                        "eventDescription": "Left FedEx origin facility",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "560048",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "ORIGIN_FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583924940000"
                        },
                        "eventType": "PU",
                        "eventDescription": "Picked up",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "560048",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "PICKUP_LOCATION"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583917787000"
                        },
                        "eventType": "OC",
                        "eventDescription": "Shipment information sent to FedEx",
                        "address": {
                            "streetLines": [],
                            "residential": False
                        },
                        "arrivalLocation": "CUSTOMER"
                    }
                ]
            }
        ]
    },
    {
        "highestSeverity": "SUCCESS",
        "notifications": [
            {
                "severity": "SUCCESS",
                "source": "trck",
                "code": "0",
                "message": "Request was successfully processed.",
                "localizedMessage": "Request was successfully processed.",
                "messageParameters": []
            }
        ],
        "duplicateWaybill": False,
        "moreData": False,
        "trackDetailsCount": 0,
        "trackDetails": [
            {
                "notification": {
                    "severity": "SUCCESS",
                    "source": "trck",
                    "code": "0",
                    "message": "Request was successfully processed.",
                    "localizedMessage": "Request was successfully processed.",
                    "messageParameters": []
                },
                "trackingNumber": "390931993491",
                "trackingNumberUniqueIdentifier": "2458916000~390931993491~FX",
                "statusDetail": {
                    "creationTime": {
                        "$numberLong": "1583884800000"
                    },
                    "code": "DL",
                    "description": "Delivered",
                    "location": {
                        "streetLines": [],
                        "city": "ahmedabad",
                        "stateOrProvinceCode": "GJ",
                        "countryCode": "IN",
                        "countryName": "India",
                        "residential": False
                    },
                    "ancillaryDetails": [
                        {
                            "reason": "11",
                            "reasonDescription": "C.O.D. payment received"
                        }
                    ]
                },
                "informationNotes": [],
                "customerExceptionRequests": [],
                "carrierCode": "FDXE",
                "operatingCompanyOrCarrierDescription": "FedEx Express",
                "otherIdentifiers": [
                    {
                        "packageIdentifier": {
                            "type": "COD_RETURN_TRACKING_NUMBER",
                            "value": "390931993506"
                        },
                        "trackingNumberUniqueIdentifier": "2458916000"
                    }
                ],
                "service": {
                    "type": "FEDEX_EXPRESS_SAVER",
                    "description": "FedEx Economy",
                    "shortDescription": "XS"
                },
                "packageWeight": {
                    "units": "KG",
                    "value": 14
                },
                "shipmentWeight": {
                    "units": "KG",
                    "value": 14
                },
                "packaging": {
                    "type": "YOUR_PACKAGING",
                    "description": "Your Packaging"
                },
                "packageSequenceNumber": 1,
                "packageCount": 1,
                "shipmentContentPieceCount": 0,
                "packageContentPieceCount": 0,
                "creatorSoftwareId": "WSXI",
                "charges": [],
                "attributes": [],
                "shipmentContents": [],
                "packageContents": [],
                "commodities": [],
                "customsOptionDetails": [],
                "specialHandlings": [
                    {
                        "type": "DELIVER_WEEKDAY",
                        "description": "Deliver Weekday",
                        "paymentType": "OTHER"
                    },
                    {
                        "type": "COD",
                        "description": "Collect On Delivery (COD)",
                        "paymentType": "OTHER"
                    },
                    {
                        "type": "RESIDENTIAL_DELIVERY",
                        "description": "Residential Delivery",
                        "paymentType": "OTHER"
                    }
                ],
                "payments": [
                    {
                        "classification": "TRANSPORTATION",
                        "type": "SHIPPER_ACCOUNT",
                        "description": "Shipper"
                    },
                    {
                        "classification": "DUTIES_AND_TAXES",
                        "type": "SHIPPER_ACCOUNT",
                        "description": "Shipper"
                    }
                ],
                "shipperAddress": {
                    "streetLines": [],
                    "city": "Bangalore",
                    "stateOrProvinceCode": "KA",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "datesOrTimes": [
                    {
                        "type": "ACTUAL_DELIVERY",
                        "dateOrTimestamp": "2020-03-11T14:31:00+05:30"
                    },
                    {
                        "type": "ACTUAL_PICKUP",
                        "dateOrTimestamp": "2020-03-07T16:27:00+05:30"
                    },
                    {
                        "type": "SHIP",
                        "dateOrTimestamp": "2020-03-07T00:00:00"
                    },
                    {
                        "type": "ACTUAL_TENDER",
                        "dateOrTimestamp": "2020-03-07T16:27:00+05:30"
                    }
                ],
                "specialInstructions": [],
                "lastUpdatedDestinationAddress": {
                    "streetLines": [],
                    "city": "AHMEDABAD",
                    "stateOrProvinceCode": "GJ",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "destinationAddress": {
                    "streetLines": [],
                    "city": "ahmedabad",
                    "stateOrProvinceCode": "GJ",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "actualDeliveryAddress": {
                    "streetLines": [],
                    "city": "ahmedabad",
                    "stateOrProvinceCode": "GJ",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "deliveryLocationType": "RESIDENCE",
                "deliveryLocationDescription": "Residence",
                "deliveryAttempts": 0,
                "deliverySignatureName": "S.SURESH",
                "pieceCountVerificationDetails": [],
                "totalUniqueAddressCountInConsolidation": 0,
                "availableImages": [
                    {
                        "type": "SIGNATURE_PROOF_OF_DELIVERY"
                    }
                ],
                "notificationEventsAvailable": [
                    "ON_DELIVERY"
                ],
                "splitShipmentParts": [],
                "deliveryOptionEligibilityDetails": [
                    {
                        "option": "INDIRECT_SIGNATURE_RELEASE",
                        "eligibility": "INELIGIBLE"
                    },
                    {
                        "option": "REDIRECT_TO_HOLD_AT_LOCATION",
                        "eligibility": "INELIGIBLE"
                    },
                    {
                        "option": "REROUTE",
                        "eligibility": "INELIGIBLE"
                    },
                    {
                        "option": "RESCHEDULE",
                        "eligibility": "INELIGIBLE"
                    }
                ],
                "events": [
                    {
                        "timestamp": {
                            "$numberLong": "1583917260000"
                        },
                        "eventType": "DL",
                        "eventDescription": "Delivered",
                        "statusExceptionCode": "11",
                        "statusExceptionDescription": "C.O.D. payment received",
                        "address": {
                            "streetLines": [],
                            "city": "ahmedabad",
                            "stateOrProvinceCode": "GJ",
                            "postalCode": "380015",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "DELIVERY_LOCATION"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583913120000"
                        },
                        "eventType": "OD",
                        "eventDescription": "On FedEx vehicle for delivery",
                        "address": {
                            "streetLines": [],
                            "city": "AHMEDABAD",
                            "stateOrProvinceCode": "GJ",
                            "postalCode": "380009",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "VEHICLE"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583896140000"
                        },
                        "eventType": "AR",
                        "eventDescription": "At local FedEx facility",
                        "address": {
                            "streetLines": [],
                            "city": "AHMEDABAD",
                            "stateOrProvinceCode": "GJ",
                            "postalCode": "380009",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "DESTINATION_FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583792820000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "AHMEDABAD",
                            "stateOrProvinceCode": "GJ",
                            "postalCode": "382213",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583792580000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "AHMEDABAD",
                            "stateOrProvinceCode": "GJ",
                            "postalCode": "382213",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583791500000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "AHMEDABAD",
                            "stateOrProvinceCode": "GJ",
                            "postalCode": "382213",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583789400000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "AHMEDABAD",
                            "stateOrProvinceCode": "GJ",
                            "postalCode": "382213",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583699460000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "NAVI MUMBAI",
                            "stateOrProvinceCode": "MH",
                            "postalCode": "410218",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583612760000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "562123",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583605440000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "562123",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583601240000"
                        },
                        "eventType": "DP",
                        "eventDescription": "Left FedEx origin facility",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "560048",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "ORIGIN_FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583578620000"
                        },
                        "eventType": "PU",
                        "eventDescription": "Picked up",
                        "address": {
                            "streetLines": [],
                            "city": "BANGALORE",
                            "stateOrProvinceCode": "KA",
                            "postalCode": "560048",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "PICKUP_LOCATION"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1583570132000"
                        },
                        "eventType": "OC",
                        "eventDescription": "Shipment information sent to FedEx",
                        "address": {
                            "streetLines": [],
                            "residential": False
                        },
                        "arrivalLocation": "CUSTOMER"
                    }
                ]
            }
        ]
    },
    {
        "highestSeverity": "SUCCESS",
        "notifications": [
            {
                "severity": "SUCCESS",
                "source": "trck",
                "code": "0",
                "message": "Request was successfully processed.",
                "localizedMessage": "Request was successfully processed.",
                "messageParameters": []
            }
        ],
        "duplicateWaybill": False,
        "moreData": False,
        "trackDetailsCount": 0,
        "trackDetails": [
            {
                "notification": {
                    "severity": "SUCCESS",
                    "source": "trck",
                    "code": "0",
                    "message": "Request was successfully processed.",
                    "localizedMessage": "Request was successfully processed.",
                    "messageParameters": []
                },
                "trackingNumber": "391080326650",
                "trackingNumberUniqueIdentifier": "2458922000~391080326650~FX",
                "statusDetail": {
                    "creationTime": {
                        "$numberLong": "1584662400000"
                    },
                    "code": "DL",
                    "description": "Delivered",
                    "location": {
                        "streetLines": [],
                        "city": "Thane",
                        "stateOrProvinceCode": "MH",
                        "countryCode": "IN",
                        "countryName": "India",
                        "residential": False
                    },
                    "ancillaryDetails": []
                },
                "informationNotes": [],
                "customerExceptionRequests": [],
                "carrierCode": "FDXE",
                "operatingCompanyOrCarrierDescription": "FedEx Express",
                "otherIdentifiers": [],
                "service": {
                    "type": "FEDEX_EXPRESS_SAVER",
                    "description": "FedEx Economy",
                    "shortDescription": "XS"
                },
                "packageWeight": {
                    "units": "KG",
                    "value": 14
                },
                "shipmentWeight": {
                    "units": "KG",
                    "value": 14
                },
                "packaging": {
                    "type": "YOUR_PACKAGING",
                    "description": "Your Packaging"
                },
                "packageSequenceNumber": 1,
                "packageCount": 1,
                "shipmentContentPieceCount": 0,
                "packageContentPieceCount": 0,
                "creatorSoftwareId": "WSXI",
                "charges": [],
                "attributes": [],
                "shipmentContents": [],
                "packageContents": [],
                "commodities": [],
                "customsOptionDetails": [],
                "specialHandlings": [
                    {
                        "type": "DELIVER_WEEKDAY",
                        "description": "Deliver Weekday",
                        "paymentType": "OTHER"
                    },
                    {
                        "type": "COD",
                        "description": "Collect On Delivery (COD)",
                        "paymentType": "OTHER"
                    }
                ],
                "payments": [
                    {
                        "classification": "TRANSPORTATION",
                        "type": "SHIPPER_ACCOUNT",
                        "description": "Shipper"
                    },
                    {
                        "classification": "DUTIES_AND_TAXES",
                        "type": "SHIPPER_ACCOUNT",
                        "description": "Shipper"
                    }
                ],
                "shipperAddress": {
                    "streetLines": [],
                    "city": "Bangalore",
                    "stateOrProvinceCode": "KA",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "datesOrTimes": [
                    {
                        "type": "ACTUAL_DELIVERY",
                        "dateOrTimestamp": "2020-03-20T16:00:00+05:30"
                    },
                    {
                        "type": "ACTUAL_PICKUP",
                        "dateOrTimestamp": "2020-03-13T17:14:00+05:30"
                    },
                    {
                        "type": "SHIP",
                        "dateOrTimestamp": "2020-03-13T00:00:00"
                    },
                    {
                        "type": "ACTUAL_TENDER",
                        "dateOrTimestamp": "2020-03-13T17:14:00+05:30"
                    }
                ],
                "specialInstructions": [],
                "lastUpdatedDestinationAddress": {
                    "streetLines": [],
                    "city": "THANE",
                    "stateOrProvinceCode": "MH",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "destinationAddress": {
                    "streetLines": [],
                    "city": "Thane",
                    "stateOrProvinceCode": "MH",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "actualDeliveryAddress": {
                    "streetLines": [],
                    "city": "Thane",
                    "stateOrProvinceCode": "MH",
                    "countryCode": "IN",
                    "countryName": "India",
                    "residential": False
                },
                "deliveryAttempts": 0,
                "deliverySignatureName": "SIGN",
                "pieceCountVerificationDetails": [],
                "totalUniqueAddressCountInConsolidation": 0,
                "availableImages": [],
                "notificationEventsAvailable": [
                    "ON_DELIVERY"
                ],
                "splitShipmentParts": [],
                "deliveryOptionEligibilityDetails": [
                    {
                        "option": "INDIRECT_SIGNATURE_RELEASE",
                        "eligibility": "INELIGIBLE"
                    },
                    {
                        "option": "REDIRECT_TO_HOLD_AT_LOCATION",
                        "eligibility": "INELIGIBLE"
                    },
                    {
                        "option": "REROUTE",
                        "eligibility": "INELIGIBLE"
                    },
                    {
                        "option": "RESCHEDULE",
                        "eligibility": "INELIGIBLE"
                    }
                ],
                "events": [
                    {
                        "timestamp": {
                            "$numberLong": "1584700200000"
                        },
                        "eventType": "DL",
                        "eventDescription": "Delivered",
                        "address": {
                            "streetLines": [],
                            "city": "Thane",
                            "stateOrProvinceCode": "MH",
                            "postalCode": "400604",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "DELIVERY_LOCATION"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1584684840000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "statusExceptionCode": "67",
                        "statusExceptionDescription": "Tendered to authorized agent for final delivery",
                        "address": {
                            "streetLines": [],
                            "city": "MUMBAI",
                            "stateOrProvinceCode": "MH",
                            "postalCode": "400078",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1584637260000"
                        },
                        "eventType": "AF",
                        "eventDescription": "At local FedEx facility",
                        "address": {
                            "streetLines": [],
                            "city": "MUMBAI",
                            "stateOrProvinceCode": "MH",
                            "postalCode": "400078",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1584601080000"
                        },
                        "eventType": "OD",
                        "eventDescription": "On FedEx vehicle for delivery",
                        "address": {
                            "streetLines": [],
                            "city": "MUMBAI",
                            "stateOrProvinceCode": "MH",
                            "postalCode": "400078",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "VEHICLE"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1584600540000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "statusExceptionCode": "67",
                        "statusExceptionDescription": "Tendered to authorized agent for final delivery",
                        "address": {
                            "streetLines": [],
                            "city": "MUMBAI",
                            "stateOrProvinceCode": "MH",
                            "postalCode": "400078",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1584552120000"
                        },
                        "eventType": "AF",
                        "eventDescription": "At local FedEx facility",
                        "address": {
                            "streetLines": [],
                            "city": "MUMBAI",
                            "stateOrProvinceCode": "MH",
                            "postalCode": "400078",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1584527400000"
                        },
                        "eventType": "DE",
                        "eventDescription": "Delivery exception",
                        "statusExceptionCode": "93",
                        "statusExceptionDescription": "Held, unable to collect payment",
                        "address": {
                            "streetLines": [],
                            "city": "MUMBAI",
                            "stateOrProvinceCode": "MH",
                            "postalCode": "400078",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "DELIVERY_LOCATION"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1584512820000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "statusExceptionCode": "67",
                        "statusExceptionDescription": "Tendered to authorized agent for final delivery",
                        "address": {
                            "streetLines": [],
                            "city": "MUMBAI",
                            "stateOrProvinceCode": "MH",
                            "postalCode": "400078",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1584508320000"
                        },
                        "eventType": "OD",
                        "eventDescription": "On FedEx vehicle for delivery",
                        "address": {
                            "streetLines": [],
                            "city": "MUMBAI",
                            "stateOrProvinceCode": "MH",
                            "postalCode": "400078",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "VEHICLE"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1584427740000"
                        },
                        "eventType": "IT",
                        "eventDescription": "In transit",
                        "statusExceptionCode": "67",
                        "statusExceptionDescription": "Tendered to authorized agent for final delivery",
                        "address": {
                            "streetLines": [],
                            "city": "MUMBAI",
                            "stateOrProvinceCode": "MH",
                            "postalCode": "400078",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "FEDEX_FACILITY"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1584424620000"
                        },
                        "eventType": "OD",
                        "eventDescription": "On FedEx vehicle for delivery",
                        "address": {
                            "streetLines": [],
                            "city": "MUMBAI",
                            "stateOrProvinceCode": "MH",
                            "postalCode": "400078",
                            "countryCode": "IN",
                            "countryName": "India",
                            "residential": False
                        },
                        "arrivalLocation": "VEHICLE"
                    },
                    {
                        "timestamp": {
                            "$numberLong": "1584378900000"
                            }
                    }
                ]
        }
        ]
    }
]
  