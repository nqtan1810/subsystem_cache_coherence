//////////////////////////////////////////////////////////////////////////////////
// this module is used to determine if a block is dirty or not 
// and generate next_state for MOESI controller both cpu and bus access
//////////////////////////////////////////////////////////////////////////////////

module moesi_controller
(
    input [2:0] hit_way_state1,     // both hit_way and evicted_way
    input [2:0] hit_way_state2,
    input hit1,
    input hit2,
    input instr_type,               // read = 0, write = 1
    input is_mem_fetch,
    input is_bus_fetch,
    input [1:0] bus_snoop,
    input is_R_R,
    
    output reg dirty,
    output reg is_exclusive,
    output reg [2:0] next_state1,
    output reg [2:0] next_state2
    
    // for demo to fix E-E bug
    // input is_E_E
    ///////////////////////////////////
);
    
    parameter M = 3'b000;
    parameter O = 3'b001;
    parameter E = 3'b010;
    parameter S = 3'b011;
    parameter I = 3'b100;
    
    always @(*) begin
        // is this block dirty or not
        if(hit_way_state1 == M || hit_way_state1 == O || hit_way_state1 == S) begin
            dirty = 1;
        end
        else begin
            dirty = 0;
        end
        
        // is exclusive or not, used to determine whether need to snoop to invalid other block in Other Cache L1
        is_exclusive = hit_way_state1 == E;
        
        // generate the next MOESI state for cpu access
        if(hit1) begin                   // hit
            if(instr_type) begin        // write hit
                next_state1 = M;
            end
            else begin                  // read hit
                next_state1 = hit_way_state1;
            end
        end 
        else                            // miss
        if(is_bus_fetch) begin       // fetch data from other cache
            // if(instr_type) begin        // probe write hit
            //     next_state1 = M;
            // end
            // else begin                  // probe read hit
            //     next_state1 = S;
            // end
            next_state1 = S;
        end 
        else
        if(is_mem_fetch) begin       // fetch data from memory
            // if(instr_type) begin    
            //     next_state1 = M;
            // end
            // else begin
            //     next_state1 = E;
            // end
            // next_state1 = E;
            if (is_R_R) 
                next_state1 = S;
            else 
                next_state1 = E;
        end
        else begin
            // next_state1 = hit_way_state1;
            next_state1 = I;
        end
        
        // generate the next MOESI state for bus access
        if(hit2) begin
            if(bus_snoop == 2'b00) begin        // other cache read      
                if(hit_way_state2 == E) begin
                    next_state2 = S;
                end
                else 
                if(hit_way_state2 == M) begin
                    next_state2 = O;
                end
                else begin
                    next_state2 = hit_way_state2;
                end
            end
            else                                // other cache write, read and request invalid
            if(bus_snoop == 2'b01) begin
                next_state2 = I;
            end
            else                                // other cache write and request invalid
            if(bus_snoop == 2'b10) begin
                next_state2 = I;
            end
            else begin
                next_state2 = hit_way_state2;
            end
        end
        else begin
            next_state2 = hit_way_state2;
        end
    end

endmodule
