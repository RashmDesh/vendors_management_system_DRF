

## Vendor Management System with Performance Metrics
Develop a Vendor Management System using Django and Django REST Framework. This
system will handle vendor profiles, track purchase orders, and calculate vendor performance
metrics. <br>
### Core Features
1. Vendor Profile Management:<br>
● Model Design: Create a model to store vendor information including name, contact
details, address, and a unique vendor code. <br>
● API Endpoints: <br>
● POST /api/vendors/: Create a new vendor.<br>
● GET /api/vendors/: List all vendors.<br>
● GET /api/vendors/{vendor_id}/: Retrieve a specific vendor's details. <br>
● PUT /api/vendors/{vendor_id}/: Update a vendor's details.<br>
● DELETE /api/vendors/{vendor_id}/: Delete a vendor. <br>

2. Purchase Order Tracking: <br>
● Model Design: Track purchase orders with fields like PO number, vendor reference,
order date, items, quantity, and status. <br>
● API Endpoints:<br>
● POST /api/purchase_orders/: Create a purchase order. <br>
● GET /api/purchase_orders/: List all purchase orders with an option to filter by
vendor.<br>
● GET /api/purchase_orders/{po_id}/: Retrieve details of a specific purchase order. <br>
● PUT /api/purchase_orders/{po_id}/: Update a purchase order.<br>
● DELETE /api/purchase_orders/{po_id}/: Delete a purchase order.<br>

3. Vendor Performance Evaluation:<br>
● Metrics: <br>
● On-Time Delivery Rate: Percentage of orders delivered by the promised date. <br>
● Quality Rating: Average of quality ratings given to a vendor’s purchase orders. <br>
● Response Time: Average time taken by a vendor to acknowledge or respond to
purchase orders. <br>
● Fulfilment Rate: Percentage of purchase orders fulfilled without issues. <br>
● Model Design: Add fields to the vendor model to store these performance metrics. <br>
● API Endpoints: <br>
● GET /api/vendors/{vendor_id}/performance: Retrieve a vendor's performance
metrics. <br>

### Data Models
1. Vendor Model <br>
This model stores essential information about each vendor and their performance metrics. <br>
● Fields: <br>
● name: CharField - Vendor's name. <br>
● contact_details: TextField - Contact information of the vendor. <br>
● address: TextField - Physical address of the vendor. <br>
● vendor_code: CharField - A unique identifier for the vendor. <br>
● on_time_delivery_rate: FloatField - Tracks the percentage of on-time deliveries. <br>
● quality_rating_avg: FloatField - Average rating of quality based on purchase 
orders. <br>
● average_response_time: FloatField - Average time taken to acknowledge
purchase orders. <br>
● fulfillment_rate: FloatField - Percentage of purchase orders fulfilled successfully. <br>
2. Purchase Order (PO) Model <br>
This model captures the details of each purchase order and is used to calculate various
performance metrics.<br>
● Fields:<br>
● po_number: CharField - Unique number identifying the PO.<br>
● vendor: ForeignKey - Link to the Vendor model. <br>
● order_date: DateTimeField - Date when the order was placed. <br>
● delivery_date: DateTimeField - Expected or actual delivery date of the order. <br>
● items: JSONField - Details of items ordered. <br>
● quantity: IntegerField - Total quantity of items in the PO. <br>
● status: CharField - Current status of the PO (e.g., pending, completed, canceled). <br>
● quality_rating: FloatField - Rating given to the vendor for this PO (nullable). <br>
● issue_date: DateTimeField - Timestamp when the PO was issued to the vendor. <br>
● acknowledgment_date: DateTimeField, nullable - Timestamp when the vendor
acknowledged the PO. <br>
3. Historical Performance Model <br>
This model optionally stores historical data on vendor performance, enabling trend analysis. <br>
● Fields: <br>
● vendor: ForeignKey - Link to the Vendor model. <br>
● date: DateTimeField - Date of the performance record. <br>
● on_time_delivery_rate: FloatField - Historical record of the on-time delivery rate. <br>
● quality_rating_avg: FloatField - Historical record of the quality rating average. <br>
● average_response_time: FloatField - Historical record of the average response 
time.<br>
● fulfillment_rate: FloatField - Historical record of the fulfilment rate. <br>
