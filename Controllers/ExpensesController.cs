using ExpenseTracker.Data;
using ExpenseTracker.Models;
using Microsoft.AspNetCore.Mvc;

namespace ExpenseTracker.Controllers
{
    public class ExpensesController : Controller
    {
        private readonly AppDbContext _context;

        public ExpensesController(AppDbContext context)
        {
            _context = context;
        }

        public IActionResult Index()
        {
            var expenses = _context.Expenses
                .OrderByDescending(e => e.Date)
                .ToList();

            return View(expenses);
        }

        public IActionResult Create()
        {
            return View();
        }

        [HttpPost]
        public IActionResult Create(Expense expense)
        {
            if (!ModelState.IsValid)
                return View(expense);

            _context.Expenses.Add(expense);
            _context.SaveChanges();

            return RedirectToAction(nameof(Index));
        }
    }
}
