import csv
import json

from dataset import data
from config import columns
from datetime import datetime
import statistics



class DataProcessor:
    def __init__(self, data):
        self.data = data
        self.delivery_days = [] # List to store the number of days taken for each delivery
        self.delivery_attempts = [] # List to store the number of delivery attempts for each delivery

    def process(self):
        json_str = json.dumps(self.data)

        try:
            self.data = json.loads(json_str)
        except json.JSONDecodeError:
            print("Error: Invalid JSON")
            exit(1)
        
        # Write the processed data to a CSV file
        try:
            with open('output.csv', 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=columns)

                writer.writeheader()

                for item in self.data:
                    self._write_row(writer, item)

            self._output_summary()
        except IOError:
            print("Error: Could not write to file")

    def _write_row(self, writer, item):
         # Process each item in the data
        trackDetails = item.get("trackDetails", [{}])
        
        for details in trackDetails:
            datesOrTimes = details.get("datesOrTimes", [{}]*3)
            shipmentWeight = details.get("shipmentWeight", {}).get("value", "")
            trackingNumber = details.get("trackingNumber", "")

            for d in datesOrTimes:
                if d.get("type", "") == "ACTUAL_PICKUP":
                    pickupdateandtime = d.get("dateOrTimestamp", "")
                elif d.get("type", "") == "ACTUAL_DELIVERY":
                    deliveryDateTime = d.get("dateOrTimestamp", "")
                elif d.get("type", "") == "SHIP":
                    outForDeliveryDateTime = d.get("dateOrTimestamp", "")

            events = details.get("events", [{}])
            delivery_event = next((e for e in events if e.get("arrivalLocation") == "DELIVERY_LOCATION"), {})
            pickup_event = next((e for e in events if e.get("arrivalLocation") == "PICKUP_LOCATION"), {})

            noOfDeliveryAttempts = 0
            for event in events:
                if (event.get("eventType", "") == "DL") or (event.get("eventType", "") == "OD"):
                    noOfDeliveryAttempts += 1

            drop_address = delivery_event.get("address", {})
            pickup_address = pickup_event.get("address", {})

            dropPincodeCityState = f"{drop_address.get('postalCode', '')} {drop_address.get('city', '')} {drop_address.get('stateOrProvinceCode', '')}"
            pickupPincodeCityState = f"{pickup_address.get('postalCode', '')} {pickup_address.get('city', '')} {pickup_address.get('stateOrProvinceCode', '')}"

            paymentType = "Prepaid" if len(details.get("statusDetail", {}).get("ancillaryDetails", [])) == 0 else "COD"

            # Calculate the number of days taken for delivery and the number of delivery attempts
            days_taken_for_delivery = (datetime.strptime(deliveryDateTime, "%Y-%m-%dT%H:%M:%S%z") - datetime.strptime(pickupdateandtime, "%Y-%m-%dT%H:%M:%S%z")).days
            self.delivery_days.append(days_taken_for_delivery)
            self.delivery_attempts.append(noOfDeliveryAttempts)

            row = {
                "Tracking number" : trackingNumber,
                "Payment type (Prepaid/COD)" : paymentType,
                "Pickup Date Time" : pickupdateandtime,
                "Delivery Date Time" : deliveryDateTime,
                "Days Taken for Delivery" : (datetime.strptime(deliveryDateTime, "%Y-%m-%dT%H:%M:%S%z") - datetime.strptime(pickupdateandtime, "%Y-%m-%dT%H:%M:%S%z")).days,
                "Out for Delivery datetime(s)" : outForDeliveryDateTime,
                "Shipment weight" : shipmentWeight,
                "Pickup Pincode, City, State" : pickupPincodeCityState,
                "Drop Pincode, City, State" : dropPincodeCityState,
                "Number of Delivery Attempts Needed" : noOfDeliveryAttempts
            }
            writer.writerow(row)
    
    def _output_summary(self):
        # Calculate the mean, median, and mode of the delivery days and delivery attempts

        summary = {
            "Mean of days taken for delivery": statistics.mean(self.delivery_days),
            "Median of days taken for delivery": statistics.median(self.delivery_days),
            "Mode of days taken for delivery": statistics.mode(self.delivery_days),
            "Mean of delivery attempts": statistics.mean(self.delivery_attempts),
            "Median of delivery attempts": statistics.median(self.delivery_attempts),
            "Mode of delivery attempts": statistics.mode(self.delivery_attempts)
        }

        # Write the summary statistics to a separate CSV file
        with open('summary.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=summary.keys())
            writer.writeheader()
            writer.writerow(summary)

processor = DataProcessor(data)
processor.process()
