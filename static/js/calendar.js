document.addEventListener("DOMContentLoaded", function () {
    const calendarContainer = document.getElementById("availability-calendar");

    // -----------------------------
    // Read data passed from Django
    // -----------------------------
    const bookedRanges = JSON.parse(
        document.getElementById("booked-dates").textContent
    );

    const pricePerNight = parseFloat(calendarContainer.dataset.price);

    // Hidden fields inside booking_create.html
    const checkInField = document.querySelector("input[name='check_in']");
    const checkOutField = document.querySelector("input[name='check_out']");

    // -----------------------------
    // Calendar state
    // -----------------------------
    let selectedCheckIn = null;
    let selectedCheckOut = null;

    // -----------------------------
    // Utility: check if a date is booked
    // -----------------------------
    function isBooked(date) {
        for (const range of bookedRanges) {
            const start = new Date(range.start);
            const end = new Date(range.end);

            if (date >= start && date < end) {
                return true;
            }
        }
        return false;
    }

    // -----------------------------
    // Render calendar (simple version)
    // -----------------------------
    function renderCalendar(year, month) {
        calendarContainer.innerHTML = "";

        const firstDay = new Date(year, month, 1);
        const lastDay = new Date(year, month + 1, 0);

        const monthName = firstDay.toLocaleString("default", { month: "long" });

        // Header
        const header = document.createElement("h2");
        header.textContent = `${monthName} ${year}`;
        calendarContainer.appendChild(header);

        // Grid
        const grid = document.createElement("div");
        grid.classList.add("calendar-grid");

        for (let day = 1; day <= lastDay.getDate(); day++) {
            const date = new Date(year, month, day);
            const cell = document.createElement("div");
            cell.classList.add("calendar-day");
            cell.textContent = day;

            // Disable booked dates
            if (isBooked(date)) {
                cell.classList.add("booked");
                cell.style.opacity = "0.4";
                cell.style.pointerEvents = "none";
            } else {
                cell.addEventListener("click", () => selectDate(date));
            }

            grid.appendChild(cell);
        }

        calendarContainer.appendChild(grid);
    }

    // -----------------------------
    // Handle date selection
    // -----------------------------
    function selectDate(date) {
        if (!selectedCheckIn) {
            selectedCheckIn = date;
            checkInField.value = date.toISOString().split("T")[0];
        } else if (!selectedCheckOut) {
            if (date <= selectedCheckIn) {
                alert("Check-out must be after check-in.");
                return;
            }

            selectedCheckOut = date;
            checkOutField.value = date.toISOString().split("T")[0];
        } else {
            // Reset selection if both already chosen
            selectedCheckIn = date;
            selectedCheckOut = null;
            checkInField.value = date.toISOString().split("T")[0];
            checkOutField.value = "";
        }

        highlightSelection();
    }

    // -----------------------------
    // Highlight selected dates
    // -----------------------------
    function highlightSelection() {
        const cells = document.querySelectorAll(".calendar-day");

        cells.forEach((cell) => {
            cell.classList.remove("selected");
        });

        if (selectedCheckIn) {
            const day = selectedCheckIn.getDate();
            cells[day - 1].classList.add("selected");
        }

        if (selectedCheckOut) {
            const day = selectedCheckOut.getDate();
            cells[day - 1].classList.add("selected");
        }
    }

    // -----------------------------
    // Initial render
    // -----------------------------
    const today = new Date();
    renderCalendar(today.getFullYear(), today.getMonth());
});
