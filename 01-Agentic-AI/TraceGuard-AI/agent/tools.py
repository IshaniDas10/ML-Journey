
def parse_logs(file_path):
    """
    Read a security log file and return its non-empty lines.
    """

    with open(file_path, "r", encoding="utf-8") as log_file:
        logs = [
            line.strip()
            for line in log_file
            if line.strip()
        ]

    return logs

def count_failed_logins(logs):
    """
    Count failed login attempts and group them by IP address.
    """

    failed_attempts = {}

    for log in logs:
        if "LOGIN_FAILED" in log:
            ip = log.split("ip=")[1].split()[0]

            if ip in failed_attempts:
                failed_attempts[ip] += 1
            else:
                failed_attempts[ip] = 1

    return failed_attempts

def extract_ips(logs):
    """
    Extract all unique IP addresses from security logs.
    """

    unique_ips = set()

    for log in logs:
        if "ip=" in log:
            ip = log.split("ip=")[1].split()[0]
            unique_ips.add(ip)

    return sorted(unique_ips)


def analyze_ip_activity(logs):
    """
    Analyze successful and failed login activity for each IP.
    """

    ip_activity = {}

    for log in logs:
        if "ip=" not in log:
            continue

        ip = log.split("ip=")[1].split()[0]

        if ip not in ip_activity:
            ip_activity[ip] = {
                "successful_logins": 0,
                "failed_logins": 0
            }

        if "LOGIN_SUCCESS" in log:
            ip_activity[ip]["successful_logins"] += 1

        elif "LOGIN_FAILED" in log:
            ip_activity[ip]["failed_logins"] += 1

    return ip_activity

def detect_suspicious_patterns(logs):
    """
    Detect IP addresses with repeated failed login attempts.
    """

    ip_activity = analyze_ip_activity(logs)

    suspicious_ips = []

    for ip, activity in ip_activity.items():

        failed = activity["failed_logins"]
        successful = activity["successful_logins"]

        if failed >= 5:

            if successful > 0:
                severity = "HIGH"
                reason = "Repeated failed logins followed by a successful login"

            else:
                severity = "MEDIUM"
                reason = "Multiple failed login attempts detected"

            suspicious_ips.append({
                "ip": ip,
                "failed_logins": failed,
                "successful_logins": successful,
                "severity": severity,
                "reason": reason
            })

    return suspicious_ips

def generate_summary(logs):
    """
    Generate an overall security analysis summary.
    """

    failed_logins = count_failed_logins(logs)
    unique_ips = extract_ips(logs)
    ip_activity = analyze_ip_activity(logs)
    suspicious_ips = detect_suspicious_patterns(logs)

    total_failed = sum(failed_logins.values())

    total_successful = sum(
        activity["successful_logins"]
        for activity in ip_activity.values()
    )

    summary = {
        "total_log_entries": len(logs),
        "total_unique_ips": len(unique_ips),
        "total_failed_logins": total_failed,
        "total_successful_logins": total_successful,
        "suspicious_ip_count": len(suspicious_ips),
        "suspicious_ips": suspicious_ips,
        "ip_activity": ip_activity
    }

    return summary
