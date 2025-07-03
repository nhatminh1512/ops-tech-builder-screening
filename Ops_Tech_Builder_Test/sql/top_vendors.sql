-- Top 5 vendors by total amount paid in the last 30 days
SELECT vendor, SUM(amount) AS total_paid
FROM invoices
WHERE status = 'paid'
  AND created_at >= CURRENT_DATE - INTERVAL '30 days'
GROUP BY vendor
ORDER BY total_paid DESC
LIMIT 5; 