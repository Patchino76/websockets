"use client";
import React, { useState } from "react";
import { Button } from "./button";
import {
  Tooltip,
  TooltipContent,
  TooltipProvider,
  TooltipTrigger,
} from "@/components/ui/tooltip";
import { MoonIcon, SunIcon } from "lucide-react";

const LightDarkToggle = () => {
  const [isDarkMode, setIsDarkMode] = useState(true);
  return (
    <div>
      <Button onClick={() => setIsDarkMode(!isDarkMode)}>
        <TooltipProvider>
          <Tooltip>
            <TooltipTrigger>{isDarkMode ? <MoonIcon /> : <SunIcon />}</TooltipTrigger>
            <TooltipContent>
              {isDarkMode ? "Позволи светла тема" : "Позволи тъмна тема"}
            </TooltipContent>
          </Tooltip>
        </TooltipProvider>
      </Button>
    </div>
  );
};

export default LightDarkToggle;
