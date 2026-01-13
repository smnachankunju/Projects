def generate_report(target, findings):
    with open("reports/report.html", "w") as f:
        f.write("<html><head><title>Vulnerability Scan Report</title></head><body>")
        f.write(f"<h1>Scan Report for {target}</h1>")

        if not findings:
            f.write("<p>No vulnerabilities found.</p>")
        else:
            f.write("<table border='1' cellpadding='8'>")
            f.write("<tr><th>Type</th><th>Action</th><th>Severity</th></tr>")

            for v in findings:
                f.write(
                    f"<tr>"
                    f"<td>{v['type']}</td>"
                    f"<td>{v['action']}</td>"
                    f"<td>{v['severity']}</td>"
                    f"</tr>"
                )

            f.write("</table>")

        f.write("</body></html>")

    print("\n[+] Report generated: reports/report.html")
