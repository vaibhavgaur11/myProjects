using EmployeeA.Models;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;


namespace EmployeeA.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class EmployeeAPIController : ControllerBase
    {
        private readonly CompanyDbContext context;

        public EmployeeAPIController(CompanyDbContext context)
        {
            this.context = context;
        }

        [HttpGet]
        public async Task<ActionResult<List<Employee>>> Get()
        {
            var data = await context.Employees.ToListAsync();

            return Ok(data);
        }

        [HttpGet("{id}")]
        public async Task<ActionResult<Employee>> GetbyID(int id)
        {
            var data = await context.Employees.FindAsync(id);
            if (data == null)
            {
                return NotFound();
            }
            return Ok(data);



        }

        [HttpPost]
        public async Task<ActionResult<Employee>> Create(Employee employee)
        {
            if (employee == null)
                return BadRequest();

            await context.Employees.AddAsync(employee);
            await context.SaveChangesAsync();

            return CreatedAtAction(
                nameof(GetbyID),
                new { id = employee.EmployeeId },
                employee);
        }

        [HttpDelete("{id}")]
        public async Task<IActionResult> Delete(int id)
        {
            var employee = await context.Employees.FindAsync(id);

            if (employee == null)
                return NotFound();

            context.Employees.Remove(employee);
            await context.SaveChangesAsync();

            return NoContent(); 
        }

        [HttpPut("{id}")]
        public async Task<IActionResult> Update(int id, Employee employee)
        {
            if (id != employee.EmployeeId)
                return BadRequest("Employee ID mismatch");

            var existingEmployee = await context.Employees.FindAsync(id);

            if (existingEmployee == null)
                return NotFound();

            // Update fields
            existingEmployee.Name = employee.Name;
            existingEmployee.Designation = employee.Designation;

            await context.SaveChangesAsync();

            return NoContent(); 
        }




    }
}
