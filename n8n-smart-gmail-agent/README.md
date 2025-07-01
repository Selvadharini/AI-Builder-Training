## Smart Gmail Agent with n8n

#### Task 
Integrate "HTTP Request" tool that makes request to URL - https://api.escuelajs.co/api/v1/users with method - GET. This will give mock users response with different roles.

Based on the input query, the model should classify the request and send the email to users with either customer or admin role.

Customer queries - Product Inquiry, General Support, Sales question, billing inquiry, and feature request
Eg - "I was charged twice for this month's subscription. Can someone from billing review my account and process a refund for the duplicate charge?"

Admin queries - Technical Escalation, System Issue, Security Concern, Data Issue, and Integration Problem
Eg - "URGENT: Our API integration is down and affecting our production systems. We need immediate technical support to resolve this critical issue."


#### Agent Flow Summary

# Smart Gmail Agent – Implementation Summary

## 1. Classify Request
- Use an AI node to label incoming text as `customer` or `admin`
- `Customer` → product, billing, support, sales, feature requests  
- `Admin` → technical failures, outages, security, data, integrations  

## 2. Select Support Contact
1. Call `GetUsers`tool → returns an array of user objects.
2. Filter by role == classification
3. Pick the any user match based on request classification.

## 3. Notify Support & Confirm to User
1. Call `SendEmail` with `emailRecipient`, `subject` and `emailBody`
2. Send the user a confirmation message to user.










